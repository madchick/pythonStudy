from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
from pathlib import Path
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
'''

people = {'puppy': ['강다니엘', '백현', '박보검', '송중기'],
          'cat': ['황민현', '시우민', '이종석', '강동원', '이종석', '이준기'],
          'bear': ['마동석', '조진웅', '조세호', '안재홍'],
          'dinosaur': ['윤두준', '이민기', '육성재', '공유', '김우빈'],
          'rabbit': ['정국', '바비', '박지훈', '수호']}

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
# https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=

# https://tiktikeuro.tistory.com/174

# https://github.com/hellock/icrawler

# https://github.com/YoongiKim/AutoCrawler



Path("./img").mkdir(parents=True, exist_ok=True)
for k, v in people.items():
    Path("./img/" + k).mkdir(parents=True, exist_ok=True)
    for person in v:
        url = baseUrl + quote_plus(person)

        ''' options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        driver = webdriver.Chrome('./chromedriver', options=options)
        driver.get(url)
        driver.implicitly_wait(2)
        elem = driver.find_element_by_tag_name("body")
        no_of_pagedowns = 75
        while no_of_pagedowns:
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.1)
            no_of_pagedowns -= 1
        
        soup = bs(driver.page_source,'html.parser')
        driver.quit() '''

        html = urlopen(url)
        soup = bs(html, "html.parser")
        
        img = soup.find_all(class_='_img', limit=1000)
        Path("./img/" + k + '/' + person).mkdir(parents=True, exist_ok=True)
        n = 1
        for i in img:
            imgUrl = i['data-source']
            with urlopen(imgUrl) as f:
                fileName = './img/' + k + '/' + person + '/' + person + '-' + "{:0>4d}".format(n)+'.jpg'
                with open(fileName,'wb') as h: # w - write b - binary
                    img = f.read()
                    h.write(img)
            n += 1
            print(fileName, end='\033[K\r')

print('\n다운로드 완료')