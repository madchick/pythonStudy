import urllib.request
from bs4 import BeautifulSoup
import csv

hdr = { 'User-Agent' : 'Mozilla/5.0' }
url = "https://www.melon.com/chart/index.htm"
req = urllib.request.Request(url, headers=hdr)
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')

lst50 = soup.select('.lst50, .lst100')
melonList = []
for i in lst50:
    temp = []
    # print(i.select_one('.rank').text, end='위 ')
    # print(i.select_one('.ellipsis.rank01').a.text, end=' ')
    # print(i.select_one('.ellipsis.rank02').a.text, end=' ')
    # print(i.select_one('.ellipsis.rank03').a.text)
    temp.append(i.select_one('.rank').text)
    temp.append(i.select_one('.ellipsis.rank01').a.text)
    temp.append(i.select_one('.ellipsis.rank02').a.text)
    temp.append(i.select_one('.ellipsis.rank03').a.text)
    melonList.append(temp)

# print(melonList[0])

with open('melon100.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['순위','아티스트','곡명','앨범'])
    writer.writerows(melonList)



