from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsobj = BeautifulSoup(html,"html.parser")

nameList = bsobj.findAll("span",{"class":"green"})
print(nameList)
for name in nameList:
    print(name.get_text())