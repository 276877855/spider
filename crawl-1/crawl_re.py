from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

def getImage(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bs_obj = BeautifulSoup(html,"html.parser")
    except AttributeError as e:
        print(e)
        return None
    return bs_obj

bsObj = getImage("http://www.pythonscraping.com/pages/page3.html")
patten = re.compile(r'\.\./img/gifts/img.*\.jpg')
images = bsObj.findAll("img",{"src":re.compile(patten)})
for image in images:
    print(image["src"])