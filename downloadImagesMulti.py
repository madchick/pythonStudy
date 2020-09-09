'''

구글 다운로드 추가
# https://tiktikeuro.tistory.com/174
# https://github.com/hellock/icrawler
# https://github.com/YoongiKim/AutoCrawler

target을 엑셀파일에서 읽어오기

중단된 경우 다시 실행시키면 완료된 부분부터 시작하도록 개선

리눅스에서 실행 안되는 문제 점검
https://blog.testproject.io/2018/02/20/chrome-headless-selenium-python-linux-servers/

'''



'''

크롬 웹브라우저 설치

selenium 설치
pip install -U selenium

크롬 드라이버 설치
https://chromedriver.chromium.org/downloads
설치된 크롬과 동일한 버전으로 설치

'''



from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


'''
target = {'puppy': ['강다니엘', '백현', '박보검', '송중기'],
          'cat': ['황민현', '시우민', '이종석', '강동원', '이종석', '이준기'],
          'bear': ['마동석', '조진웅', '조세호', '안재홍'],
          'dinosaur': ['윤두준', '이민기', '육성재', '공유', '김우빈'],
          'rabbit': ['정국', '바비', '박지훈', '수호']}
'''
target = {'puppy': ['강다니엘', '백현']}

downloadFolder = './img/'



nameTag = 'google'
baseUrl = 'https://image.google.com/search?q='

Path(downloadFolder).mkdir(parents=True, exist_ok=True)
for k, v in target.items():
    Path(downloadFolder + k).mkdir(parents=True, exist_ok=True)
    for person in v:
        url = baseUrl + quote_plus(person)

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('log-level=3')
        options.add_argument("enable-automation")
        options.add_argument("dns-prefetch-disable")
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        options.add_argument("no-sandbox") 
        options.add_argument("disable-setuid-sandbox") 
        options.add_argument("disable-dev-shm-using") 
        options.add_argument("disable-extensions")
        driver = webdriver.Chrome('./chromedriver', options=options)
        print('\n' + nameTag + ' - search & feching images... (max around 500) - ' + k + ' : ' + person)
        driver.get(url)
        driver.implicitly_wait(2)
        image_btn = driver.find_element_by_css_selector('#hdtb-msb-vis > div:nth-child(2) > a')
        driver.execute_script("arguments[0].click();", image_btn)
        driver.implicitly_wait(2)
        elem = driver.find_element_by_tag_name("body")
        no_of_pagedowns = 50
        while no_of_pagedowns:
            elem.send_keys(Keys.END)
            time.sleep(0.1)
            more_btn = driver.find_element_by_css_selector('#islmp > div > div > div > div > div.YstHxe > input')
            driver.execute_script("arguments[0].click();", more_btn)
            no_of_pagedowns -= 1
        
        soup = bs(driver.page_source,'html.parser')
        #file = open('DS.html', 'w')
        #file.write(driver.page_source)
        #file.close()
        driver.quit() 

        #html = urlopen(url)
        #soup = bs(html, "html.parser")
        
        img = soup.find_all(class_="rg_i Q4LuWd", limit=3000)
        Path(downloadFolder + k + '/' + person).mkdir(parents=True, exist_ok=True)
        n = 1
        for i in img:
            try:
                imgUrl = i['src']
            except:
                imgUrl = i['data-src']
            try:
                fileUrl =  urlopen(imgUrl)
            except:
                continue
            else:
                fileName = downloadFolder + k + '/' + person + '/' + person + '-' + nameTag + '-' + "{:0>4d}".format(n)+'.jpg'
                fileLocal = open(fileName,'wb')
                img = fileUrl.read()
                fileLocal.write(img)
            n += 1
            print('download files : ' + fileName, end='\033[K\r')

print('\n' + nameTag + ' 다운로드 완료')



nameTag = 'daum'
baseUrl = 'https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q='

Path(downloadFolder).mkdir(parents=True, exist_ok=True)
for k, v in target.items():
    Path(downloadFolder + k).mkdir(parents=True, exist_ok=True)
    for person in v:
        url = baseUrl + quote_plus(person)

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument("enable-automation")
        options.add_argument("dns-prefetch-disable")
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        options.add_argument("no-sandbox") 
        options.add_argument("disable-setuid-sandbox") 
        options.add_argument("disable-dev-shm-using") 
        options.add_argument("disable-extensions")    
        driver = webdriver.Chrome('./chromedriver', options=options)
        print('\n' + nameTag + ' - search & feching images... (max around 2,500) - ' + k + ' : ' + person)
        driver.get(url)
        driver.implicitly_wait(2)
        elem = driver.find_element_by_tag_name("body")
        no_of_pagedowns = 80
        while no_of_pagedowns:
            elem.send_keys(Keys.END)
            time.sleep(0.1)
            more_btn = driver.find_element_by_css_selector('#imgColl > div.extend_comp.extend_imgtab > a.expender.open')
            driver.execute_script("arguments[0].click();", more_btn)
            no_of_pagedowns -= 1
        
        soup = bs(driver.page_source,'html.parser')
        driver.quit() 
       
        img = soup.find_all(class_="thumb_img", limit=3000)
        Path(downloadFolder + k + '/' + person).mkdir(parents=True, exist_ok=True)
        n = 1
        for i in img:
            imgUrl = i['src']
            try:
                fileUrl =  urlopen(imgUrl)
            except:
                continue
            else:
                fileName = downloadFolder + k + '/' + person + '/' + person + '-' + nameTag + '-' + "{:0>4d}".format(n)+'.jpg'
                fileLocal = open(fileName,'wb')
                img = fileUrl.read()
                fileLocal.write(img)
            n += 1
            print('download files : ' + fileName, end='\033[K\r')

print('\n' + nameTag + ' 다운로드 완료')



nameTag = 'naver'
baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='

Path(downloadFolder).mkdir(parents=True, exist_ok=True)
for k, v in target.items():
    Path(downloadFolder + k).mkdir(parents=True, exist_ok=True)
    for person in v:
        url = baseUrl + quote_plus(person)

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument("enable-automation")
        options.add_argument("dns-prefetch-disable")
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        options.add_argument("no-sandbox") 
        options.add_argument("disable-setuid-sandbox") 
        options.add_argument("disable-dev-shm-using") 
        options.add_argument("disable-extensions")
        driver = webdriver.Chrome('./chromedriver', options=options)
        print('\n' + nameTag + ' - search & feching images... (max 1,000) - ' + k + ' : ' + person)
        driver.get(url)
        driver.implicitly_wait(2)
        elem = driver.find_element_by_tag_name("body")
        no_of_pagedowns = 25
        while no_of_pagedowns:
            elem.send_keys(Keys.END)
            time.sleep(0.1)
            more_btn = driver.find_element_by_css_selector('#_sau_imageTab > div.photowall._photoGridWrapper > div.more_img > a')
            driver.execute_script("arguments[0].click();", more_btn)
            no_of_pagedowns -= 1
        
        soup = bs(driver.page_source,'html.parser')
        driver.quit() 

        img = soup.find_all(class_='_img', limit=1000)
        Path(downloadFolder + k + '/' + person).mkdir(parents=True, exist_ok=True)
        n = 1
        for i in img:
            imgUrl = i['src']
            try:
                fileUrl =  urlopen(imgUrl)
            except:
                continue
            else:
                fileName = downloadFolder + k + '/' + person + '/' + person + '-' + nameTag + '-' + "{:0>4d}".format(n)+'.jpg'
                fileLocal = open(fileName,'wb')
                img = fileUrl.read()
                fileLocal.write(img)
            n += 1
            print('download files : ' + fileName, end='\033[K\r')

print('\n' + nameTag + ' 다운로드 완료')



