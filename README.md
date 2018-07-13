# Python Spider

* [CSDN博客](https://blog.csdn.net/u014793102 "悬停显示")

## 目录


* [爬虫实战](#爬虫实战)
    * [百度文库文章下载_rev2](https://github.com/duke-coding/python-spider/blob/master/baiduwenku_pro_1.py "悬停显示")
    * [《火影忍者》漫画下载](https://github.com/duke-coding/python-spider/tree/master/cartoon "悬停显示")
    * [抖音App视频下载_rev1](https://github.com/duke-coding/python-spider/blob/master/douyin.py "悬停显示")
    * [抖音App视频下载_rev2](https://github.com/duke-coding/python-spider/blob/master/douyin_pro.py "悬停显示")
    * [抖音App视频下载_rev3](https://github.com/duke-coding/python-spider/blob/master/douyin_pro_2.py "悬停显示")
    * [12306抢票小助手](https://github.com/duke-coding/python-spider/blob/master/12306.py "悬停显示")
    * [百万英雄答题辅助系统](https://github.com/duke-coding/python-spider/tree/master/baiwan "悬停显示")   
    * [网易云音乐批量下载](https://github.com/duke-coding/python-spider/tree/master/Netease "悬停显示")
    * [B站视频和弹幕批量下载](https://github.com/duke-coding/python-spider/tree/master/bilibili "悬停显示")
    * [京东商品晒单图下载](https://github.com/duke-coding/python-spider/tree/master/jd "悬停显示")
* [其它](#其它)


## 爬虫实战

 
 * baiduwenku.py: 百度文库word文章爬取

  原理说明：http://blog.csdn.net/c406495762/article/details/72331737

  代码不完善，没有进行打包，不具通用性，纯属娱乐，以后有时间会完善。

 * carton: 使用Scrapy爬取《火影忍者》漫画

  代码可以爬取整个《火影忍者》漫画所有章节的内容，保存到本地。更改地址，可以爬取其他漫画。保存地址可以在settings.py中修改。

  动漫网站：http://comic.kukudm.com/

  原理说明：http://blog.csdn.net/c406495762/article/details/72858983

 * douyin.py:抖音App视频下载

  抖音App的视频下载，就是普通的App爬取。

 * douyin_pro:抖音App视频下载（升级版）

  抖音App的视频下载，添加视频解析网站，支持无水印视频下载，使用第三方平台解析。

 * douyin_pro_2:抖音App视频下载（升级版2）

  抖音App的视频下载，添加视频解析网站，支持无水印视频下载，通过url解析，无需第三方平台。

  动态示意图：

  ![image](https://github.com/Jack-Cherish/Pictures/blob/master/14.gif)

 * geetest.py:GEETEST验证码破解

    爬虫最大的敌人之一是什么？没错，验证码！Geetest作为提供验证码服务的行家，市场占有率还是蛮高的。遇到Geetest提供的滑动验证码怎么破？授人予鱼不如授人予渔，接下来就为大家呈现本教程的精彩内容。

    动态示意图：

    ![image](https://github.com/Jack-Cherish/Pictures/blob/master/spider_2_1.gif)

 * 12306.py:用Python抢火车票简单代码

  可以自己慢慢丰富，蛮简单，有爬虫基础很好操作，没有原理说明。

 * baiwan:百万英雄辅助答题

  效果图：

  ![image](https://github.com/Jack-Cherish/Pictures/blob/master/11.gif)

  	功能介绍：

  服务器端，使用Python（baiwan.py）通过抓包获得的接口获取答题数据，解析之后通过百度知道搜索接口匹配答案，将最终匹配的结果写入文件（file.txt)。

  手机抓包不会的朋友，可以看下我的早期[手机APP抓包教程](http://blog.csdn.net/c406495762/article/details/76850843 "悬停显示")。

  Node.js（app.js）每隔1s读取一次file.txt文件，并将读取结果通过socket.io推送给客户端（index.html）。

  亲测答题延时在3s左右。

  声明：没做过后端和前端，花了一天时间，现学现卖弄好的，javascript也是现看现用，百度的程序，调试调试而已。可能有很多用法比较low的地方，用法不对，请勿见怪，有大牛感兴趣，可以自行完善。

 * Netease:根据歌单下载网易云音乐
  	
  效果图：

  ![image](https://github.com/Jack-Cherish/Pictures/blob/master/13.gif)

  原理说明：

  暂无

  功能介绍：

  根据music_list.txt文件里的歌单的信息下载网易云音乐，将自己喜欢的音乐进行批量下载。

 * bilibili：B站视频和弹幕批量下载
  	
  原理说明：

  暂无

  使用说明：

       python bilibili.py -d 猫 -k 猫 -p 10
      
       三个参数：
       -d	保存视频的文件夹名
       -k	B站搜索的关键字
       -p	下载搜索结果前多少页

 * jd：京东商品晒单图下载

    效果图：

    ![image](https://github.com/Jack-Cherish/Pictures/blob/master/jd.gif)
    	
    原理说明：

    暂无

    使用说明：

        python jd.py -k 芒果
        
        三个参数：
        -d	保存图片的路径，默认为fd.py文件所在文件夹
        -k	搜索关键词
        -n  	下载商品的晒单图个数，即n个商店的晒单图
