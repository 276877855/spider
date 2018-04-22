## 初见网络爬虫

## 一 基础爬取

#### 1. 获取网页内容

urllib是Python的标准库，包含了从网络请求数据，处理cookie，甚至改变像请求头和用户代理这些元数据的函数 

```python
from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())
```

#### 2. Beautifulsoup

通过定位 HTML 标签来格式化和组织复杂的网络信息，用简单易用的 Python 对象为我们展现 XML 结构信息。

安装beautifulsoup

```python
 #Linux 系统
$sudo apt-get install python-bs4
 #Mac 系统
$sudo easy_install pip
$pip install beautifulsoup4

```



#### 3.第一个例子

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(),"html.parser")
print(bsObj.h1)
```

导入 urlopen，然后调用 html.read() 获取网页的 HTML 内容。这样就可以把 HTML 内容传到 BeautifulSoup 对象，转换成下面的结构 :

```html
 html → <html><head>...</head><body>...</body></html>
	— head → <head><title>A Useful Page<title></head>
		— title → <title>A Useful Page</title>
	— body → <body><h1>An Int...</h1><div>Lorem ip...</div></body>
		— h1 → <h1>An Interesting Title</h1>
		— div → <div>Lorem Ipsum dolor...</div>
```

从网页中提取的 <h1> 标签被嵌在 BeautifulSoup 对象 bsObj 结构的第二层

（html → body → h1）。不过从对象里提取 h1 标签的时候，可以直接调用它：

bsObj.h1 

下面这些函数调用都可以达到同样的效果。

```python
bsObj.html.body.h1
bsObj.body.h1
bsObj.html.h1
```



#### 4.异常处理

```python
try:
	html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
	print(e)
	# 返回空值，中断程序，或者执行另一个方案
else:
	# 程序继续。注意：如果你已经在上面异常捕捉那一段代码里返回或中断（break），
	# 那么就不需要使用else语句了，这段代码也不会执行
```

当自己调用标签不存在，也会导致错误的发生。因此，也要对调用标签出现异常时进行处理。因此对上述两种异常进行综合处理：

```python
try:
	badContent = bsObj.nonExistingTag.anotherTag
except AttributeError as e:
	print("Tag was not found")
else:
	if badContent == None:
		print ("Tag was not found")
	else:
		print(badContent)
```

用异常处理方法对上个例子进行重写:

```python
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read(),"html.parser")
		title = bsObj.body.h1
	except AttributeError as e:
		return None
	return title
title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
	print("Title could not be found")
else:
	print(title)
```



#### 5. 通过css来抓取所需结果

抓取css中所有指定的标签

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)
nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
	print(name.get_text())
```

在这里使用了.get_text()获取标签内的文本内容，那什么时候用get_text()？什么时候保留标签呢？

​	.get_text() 会把你正在处理的 HTML 文档中所有的标签都清除，然后返回
一个只包含文字的字符串。 假如你正在处理一个包含许多超链接、段落和标
签的大段源代码， 那么 .get_text() 会把这些超链接、段落和标签都清除掉，
只剩下一串不带标签的文字。

​	用 BeautifulSoup 对象查找你想要的信息，比直接在 HTML 文本里查找信
息要简单得多。 通常在你准备打印、存储和操作数据时，应该最后才使
用 .get_text()。

一般情况下，你应该尽可能地保留 HTML 文档的标签结构。 

#### 6. BeautifulSoup的find()和findAll()

定义：

find(tag, attributes, recursive, text, keywords) 

findAll(tag, attributes, recursive, text, limit, keywords)

参数的含义：

> *标签参数 tag* —可以传一个标签的名称或多个标签名称组成的 Python列表做标签参数。

.findAll({"h1","h2","h3","h4","h5","h6"}) 

> *属性参数 attributes*—用一个 Python 字典封装一个标签的若干属性和对应的属性值。 

.findAll("span", {"class":{"green", "red"}}) 

> *递归参数 recursive* 是一个布尔变量 。

默认值是true，会去查找标签的子标签，如果设为false，只会查一级标签。

> *文本参数 text* 有点不同，它是用标签的文本内容去匹配，而不是用标签的属性。 

```python
nameList = bsObj.findAll(text="the prince")
print(len(nameList)) 

```

> 范围限制参数 limit -只用于findAll方法。find其实就是findAll的limit等于1时的情形。

> 关键词参数 keyword，可以让你选择那些具有指定属性的标签。 

任何用关键词参数能够完成的任务，同样可以用其他技术解决。

 

#### 7. 处理层级标签

给定一个指定的页面结构如下所示：

```html
 html
	— body
		— div.wrapper
			— h1
			— div.content
			— table#giftList
			— tr
				— th
				— th
				— th
				— th
			— tr.gift#gift1
				— td
				— td
					— span.excitingNote
				— td
				— td
					— img
			— ……其他表格行省略了……
		— div.footer
```

处理子标签和其后代标签

```python
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
#子标签处理
def getChild(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsobj = BeautifulSoup(html,"html.parser")
    except AttributeError as e:
        return None
    return bsobj
bs_obj = getChild("http://www.pythonscraping.com/pages/page3.html")
for child in bs_obj.find("table",{"id":"giftList"}).children:
    print(child)
```

处理兄弟标签：

```python
def getSibling(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html,"html.parser")
    except AttributeError as e:
        print(e)
        return None
    return bsObj
bs_obj = getSibling("http://www.pythonscraping.com/pages/page3.html")
for sibling in bs_obj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)
```

​	如果我们选择 bsObj.table.tr 或直接就用 bsObj.tr 来获取表格中的第一行，上面的代码也可以获得正确的结果。 但是，我们还是采用更长的形式写了一行代码，这可以避免各种意外：bsObj.find("table",{"id":"giftList"}).tr
	即使页面上只有一个表格（或其他目标标签），只用标签也很容易丢失细节。另外，页面布局总是不断变化的。一个标签这次是在表格中第一行的位置，没准儿哪天就在第二行或第三行了。 如果想让你的爬虫更稳定，最好还是让标签的选择更加具体。如果有属性，就利用标签的属性。 

处理父标签：

在爬虫抓取网页时，查找父标签的次数很少，但是还需要了解一下。

```python
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
```



#### 8.正则表达式和BeautifulSoup

注意观察网页上有几个商品图片——它们的源代码形式如下：
<img src="../img/gifts/img3.jpg"> 

用正则表达式对其进行截取查找

```python
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
```



#### 9. 获取属性

```python
myTag.attrs
```

要注意这行代码返回的是一个 Python 字典对象，可以获取和操作这些属性。比如要获取图片的资源位置 src，可以用下面这行代码：
myImgTag.attrs["src"] 

#### 10. Lambda表达式

Lambda 表达式本质上就是一个函数， 可以作为其他函数的变量使用；也就是说，一个函
数不是定义成 f(x, y)，而是定义成 f(g(x), y)，或 f(g(x), h(x)) 的形式。 

```python
下面的代码就是获取有两个属性的标签：
soup.findAll(lambda tag: len(tag.attrs) == 2)
这行代码会找出下面的标签：
<div class="body" id="content"></div>
<span style="color:red" class="title"></span>
```

#### 11.其他库

lxml
这个库（http://lxml.de/） 可以用来解析 HTML 和 XML 文档，以非常底层的实现而闻名
于世，大部分源代码是用 C 语言写的。虽然学习它需要花一些时间（其实学习曲线越
陡峭，表明你可以越快地学会它），但它在处理绝大多数 HTML 文档时速度都非常快。 



