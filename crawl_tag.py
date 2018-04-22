from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
#子标签处理
# def getChild(url):
#     try:
#         html = urlopen(url)
#     except HTTPError as e:
#         return None
#     try:
#         bsobj = BeautifulSoup(html,"html.parser")
#     except AttributeError as e:
#         return None
#     return bsobj
# bs_obj = getChild("http://www.pythonscraping.com/pages/page3.html")
# for child in bs_obj.find("table",{"id":"giftList"}).children:
#     print(child)

#兄弟标签
# def getSibling(url):
#     try:
#         html = urlopen(url)
#     except HTTPError as e:
#         print(e)
#         return None
#     try:
#         bsObj = BeautifulSoup(html,"html.parser")
#     except AttributeError as e:
#         print(e)
#         return None
#     return bsObj
# bs_obj = getSibling("http://www.pythonscraping.com/pages/page3.html")
# for sibling in bs_obj.find("table",{"id":"giftList"}).tr.next_siblings:
#     print(sibling)

#父标签
def getParent(url):
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
bsObj = getParent("http://www.pythonscraping.com/pages/page3.html")
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
