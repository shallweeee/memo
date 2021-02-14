#! /usr/bin/env python3

import argparse
import logging
import os
import re
import shutil
import time

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfparser import PDFEncryptionError, PDFSyntaxError
from pdfminer.psparser import PSEOF
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine

from concurrent.futures import ThreadPoolExecutor

from functools import wraps
import signal

USE_THREADS = False
detail = False
tracking = False

year_pat = re.compile(r'(?<!\d)((19|20)\d{2})(?!\d)')


def log(msg):
    print(msg)


def track(msg):
    global tracking
    if tracking:
        print(msg)


class TimeoutError(Exception):
    pass


def timeout(seconds=15):
    def decorate(func):
        def handler(sig, frame):
            raise TimeoutError('Timed out')

        @wraps(func)
        def wrapper(*args, **kwargs):
            old = signal.signal(signal.SIGALRM, handler)
            signal.setitimer(signal.ITIMER_REAL, seconds)

            try:
                return func(*args, **kwargs)
            except TimeoutError as e:
                raise e
            finally:
                signal.setitimer(signal.ITIMER_REAL, 0)
                signal.signal(signal.SIGALRM, old)

        return wrapper

    return decorate


class Stat:
    def __init__(self, name):
        self.name = name
        self.size = os.path.getsize(name)
        self.time = []

    def record(self):
        self.time.append(time.time())

    def __str__(self):
        dt = len(self.time) > 0 and self.time[-1] - self.time[0] or 0
        deltas = [round(self.time[i] - self.time[i - 1], 3)
                  for i in range(1, len(self.time))]
        return f'{self.name} sz {self.size} dt {dt:.2f} deltas {deltas}'


def extract_year(line):
    m = year_pat.findall(line)
    if m:
        return m[-1][0]

    if line.rstrip()[-1] == '©':
        return 'next'

    log(f'### {line} ###')
    return 'none'


def find_year(pages, interpreter, device):
    prev_line = ''
    for i, page in enumerate(pages):
        track(f'page {i+1}')

        interpreter.process_page(page)
        layout = device.get_result()

        for lt in layout:
            if not (isinstance(lt, LTTextBox) or isinstance(lt, LTTextLine)):
                continue

            for line in lt.get_text().split('\n'):
                track(line)

                if prev_line:
                    line = f'{prev_line} {line}'
                    prev_line = ''

                if line.find('Copyright') != -1 or line.find('©') != -1:
                    year = extract_year(line)
                    if year == 'next':
                        prev_line = line
                        continue
                    if year:
                        return year

    return ''


@timeout()
def set_doc_parser(doc, parser):
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize('')


def find_released_year(pdf, stat):
    with open(pdf, 'rb') as f:
        stat.record()
        parser = PDFParser(f)
        doc = PDFDocument()
        set_doc_parser(doc, parser)

        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        stat.record()
        year = find_year(doc.get_pages(), interpreter, device)

        device.close()
        return year


def make_directory(path):
    os.makedirs(path, exist_ok=True)


def move_file(pdf, dest):
    for ext in ['pdf', 'epub', 'mobi', 'zip']:
        name = pdf[:-3] + ext
        if os.path.isfile(name):
            log(f'  move {name} to {dest}')
            shutil.move(name, dest)


def classify(pdf):
    log(pdf)
    stat = Stat(pdf)
    try:
        year = find_released_year(pdf, stat)
        year = year and year or 'none'
    except (TimeoutError, PDFEncryptionError, PDFSyntaxError,
            TypeError, KeyError, PSEOF) as e:
        log(f'  {e}')
        year = 'unknown'
    finally:
        stat.record()

    if year == 'none' or year == 'unknown':
        m = year_pat.findall(pdf)
        if m:
            log('  Detected from file name')
            year = m[-1][0]

    target_dir = f'{args.base}/{year}'
    make_directory(target_dir)
    move_file(pdf, target_dir)
    if detail:
        log(f'  {stat}')


def main(args):
    global detail
    global tracking
    detail = args.stat
    tracking = args.track

    if not args.warning:
        logging.propagate = False
        logging.getLogger().setLevel(logging.ERROR)

    if USE_THREADS:
        jobs = args.jobs == 0 and os.cpu_count() or args.jobs

        log(f'Pool size: {jobs}')
        with ThreadPoolExecutor(max_workers=jobs) as executor:
            executor.map(classify, args.pdfs)
    else:
        for pdf in args.pdfs:
            classify(pdf)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Classify pdf')
    parser.add_argument('pdfs', metavar='pdf', nargs='+', help='pdf file')
    parser.add_argument('-b', '--base', default='ebooks',
                        help='base directory')
    if USE_THREADS:
        parser.add_argument('-j', '--jobs', type=int, default=1,
                            help='job number')
    parser.add_argument('-s', dest='stat', action='store_true',
                        default=False, help='show statatistics')
    parser.add_argument('-t', dest='track', action='store_true',
                        default=False, help='show tracking')
    parser.add_argument('-w', dest='warning', action='store_true',
                        default=False, help='show warning')
    args = parser.parse_args()
    main(args)
