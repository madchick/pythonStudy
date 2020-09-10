from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
from pathlib import Path

from openpyxl import load_workbook

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys
import time



'''
# 테스트용 데이터
target = {'강아지': ['강아지', '멍멍이', '댕댕이']}
searchKeyword = '강아지'
searchKeywordList = []
searchKeywordList.append('강아지')
searchKeywordList.append('멍멍이')
searchKeywordList.append('댕댕이')
target = {}
target[searchKeyword] = searchKeywordList
print(target)
'''



if len(sys.argv) > 1:
    excelFileName = sys.argv[1]
else:
    excelFileName = 'downloadImagesMulti.xlsx'

downloadFolder = './img/'



load_wb = load_workbook('./' + excelFileName, data_only=True)
get_cells = load_wb['Sheet1']

target = {}
searchKeywordList = []
rowNum = 0
for row in get_cells:
    rowNum += 1
    colNum = 1
    searchKeywordList = []
    for cell in row:
        if cell.value:
            if colNum == 1:
                searchKeyword = cell.value
            searchKeywordList.append(cell.value)
        if len(row) == colNum:
            target[searchKeyword] = searchKeywordList
        colNum += 1
# print(target)



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
            print('download files : ' + fileName, end='\r')
            # print('download files : ' + fileName, end='\033[K\r')

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
            print('download files : ' + fileName, end='\r')

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
            print('download files : ' + fileName, end='\r')

print('\n' + nameTag + ' 다운로드 완료')



