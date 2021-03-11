import logging
import logging.handlers

formatter = logging.Formatter('%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

log = logging.getLogger('test_logger')
log.setLevel(logging.DEBUG)

h1 = logging.StreamHandler()
h1.setFormatter(formatter)
log.addHandler(h1)

h2 = logging.handlers.RotatingFileHandler('./test.log', maxBytes=1024 * 1024, backupCount=5)
h2.setFormatter(formatter)
log.addHandler(h2)

log.debug('hello debug')
log.info('hello info')
log.warning('hello warning')
log.error('hello error')
log.critical('hello critical')
