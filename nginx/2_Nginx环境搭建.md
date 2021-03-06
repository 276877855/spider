# lnm环境搭建

## 前置条件

1. 配置防火墙

```shell
sudo ufw disable
```
2. 系统约定

```shell
软件源代码包存放位置：/tool/lnmp
源码包编译安装位置：/usr/local/软件名
```



## 安装编译工具及库文件

```shell
使用apt-get安装
sudo apt-get install -y make  gcc g++ cmake   openssl   libxml2  libncurses5-dev bison
```
## 软件安装篇

~~~
源码安装
#1 解压
#2 切换到安装目录，执行 ./configure
#3 编译  make
#4 安装  sudo make install
~~~



```shell
1、安装cmake
tar -zxvf cmake-2.8.7.tar.gz
cd cmake-2.8.7
./configure --prefix=/usr/local/cmake
make #编译
sudo make install #安装
sudo vim /etc/profile 在path路径中增加cmake执行文件路径
export PATH=$PATH:/usr/local/cmake/bin
source /etc/profile使配置立即生效
```


```shell
2、安装pcre
cd ..
tar -zxvf pcre-8.39.tar.gz
cd pcre-8.39
./configure --prefix=/usr/local/pcre 
make && sudo make install

3、安装libmcrypt
cd ..
tar -zxvf libmcrypt-2.5.8.tar.gz
cd libmcrypt-2.5.8
./configure #配置
make #编译
sudo make install #安装

```


```shell
4、安装 nginx

tar -zxvf nginx-1.11.5.tar.gz
sudo groupadd www #添加www组
sudo useradd -g www www -s /sbin/nologin #创建nginx运行账户www并加入到www组，不允许www用户直接登录系统

#解压openssl
tar -zxvf openssl-1.1.0b.tar.gz
cd nginx-1.11.5
./configure --prefix=/usr/local/nginx --without-http_memcached_module --user=www --group=www   --with-http_stub_status_module --with-openssl=/tool/openssl-1.1.0b --with-pcre=/tool/pcre-8.39   --with-http_ssl_module
注意:--with-pcre=/src/pcre-8.39指向的是源码包解压的路径，而不是安装的路径，否则会报错
```


```shell
make
sudo make install
/usr/local/nginx/sbin/nginx #启动nginx
设置nginx开启启动
vi /etc/init.d/nginx #编辑启动文件添加下面内容
=======================================================
#!/bin/sh
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: starts the nginx web server
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
DESC="nginx daemon"
NAME=nginx
DAEMON=/usr/local/nginx/sbin/$NAME
CONFIGFILE=/usr/local/nginx/conf/$NAME.conf
PIDFILE=/usr/local/nginx/logs/$NAME.pid
SCRIPTNAME=/etc/init.d/$NAME
     
set -e
[ -x "$DAEMON" ] || exit 0
  
do_start() {
 $DAEMON -c $CONFIGFILE || echo -n "nginx already running"
}
  
do_stop() {
 kill -INT `cat $PIDFILE` || echo -n "nginx not running"
}
  
do_reload() {
 kill -HUP `cat $PIDFILE` || echo -n "nginx can't reload"
}
  
case "$1" in
 start)
 echo -n "Starting $DESC: $NAME"
 do_start
 echo "."
 ;;
 stop)
 echo -n "Stopping $DESC: $NAME"
 do_stop
 echo "."
 ;;
 reload|graceful)
 echo -n "Reloading $DESC configuration..."
 do_reload
 echo "."
 ;;
 restart)
 echo -n "Restarting $DESC: $NAME"
 do_stop
 do_start
 echo "."
 ;;
 *)
 echo "Usage: $SCRIPTNAME {start|stop|reload|restart}" >&2
 exit 3
 ;;
esac
  
exit 0
=======================================================
:wq! #保存退出
sudo chmod 775 /etc/init.d/nginx #赋予文件执行权限
sudo sysv-rc-conf #设置开机启动
/etc/rc.d/init.d/nginx restart #重新启动Nginx  stop 停止  start 启动
或者
service nginx restart
=======================================================
```



	6、配置nginx
	vi /usr/local/nginx/conf/nginx.conf
	修改/usr/local/nginx/conf/nginx.conf 配置文件,需做如下修改

```shelle
	user www www; #首行user去掉注释,修改Nginx运行组为www www；
	worker_processes 1;
	events { 
	worker_connections 1024;
	}
	http {
		include mime.types;
		default_type application/octet-stream;
		sendfile on;
		keepalive_timeout 65;
		server {
			listen 80;
			server_name localhost;
				location / {
				root /data/www;
				index index.php index.html index.htm;
				}
		}
	}

	mkdir -p /data/www
	chown www:www /data/www/ -R #设置目录所有者
	chmod 700 /data/www -R #设置目录权限
	
	#服务器相关操作命令
    service nginx restart #重启nginx

```



## 配置vhost 

```
cd /usr/local/nginx/conf 
mkdir vhost 
vim /usr/local/nginx/conf/nginx.conf

#每个语句后都要有分号
倒数第二行  加入 include /usr/local/nginx/conf/vhost/*.conf;

cd  vhost 
vim www.blog.com.conf
server {
        listen       80;
        listen       localhost:80;
        server_name  www.blog.com blog.com;

        location / {
            root   /data/www/www.blog.com;
            index  index.html index.php index.htm;
        }
    }


重启 nginx 服务   service nginx restart  


#到/data/www下建立子目录www.blog.com
mkdir /data/www/www.blog.com

cd /data/www/www.blog.com
vim index.html

:wq  保存



配置  window 的hosts 
10.0.112.155 www.blog.com

sudo /usr/local/nginx/sbin/nginx -c  /usr/local/nginx/conf/nginx.conf


sudo /usr/local/nginx/sbin/nginx -s reload

```

