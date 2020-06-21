from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://www.daum.net/')
soup = BeautifulSoup(response, 'html.parser')

i = 1
f = open("새파일.txt", 'w')
for anchor in soup.select("a.link_favorsch"):
    data = str(i) + "위: " + anchor.get_text() + "\n"
    i += 1
    f.write(data)
f.close()