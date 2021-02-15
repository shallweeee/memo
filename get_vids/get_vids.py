from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import time

url = '주소를 쓰세요'

GET_HEIGHT = '''
return Math.max(
    document.body.scrollHeight, document.documentElement.scrollHeight,
    document.body.offsetHeight, document.documentElement.offsetHeight,
    document.body.clientHeight, document.documentElement.clientHeight
)
'''

init_interval = 2
loop_interval = 2

driver = Chrome()
driver.maximize_window()

driver.get(url) 
time.sleep(init_interval)

prev_height = driver.execute_script(GET_HEIGHT)

for i in range(10000):
    driver.execute_script(f'window.scrollTo(0, {prev_height})')
    time.sleep(loop_interval)

    height = driver.execute_script(GET_HEIGHT)
    print(f'scroll {i+1} h {height}')
    if height == prev_height:
        break
    prev_height = height

page_source = driver.page_source
driver.quit()

bs = BeautifulSoup(page_source, 'lxml')
links = bs.find_all('a', {'id': 'video-title'})
vids = [link.attrs['href'].split('=')[1] for link in links]

with open('vids.txt', 'wt') as f:
    f.write('\n'.join(vids))
