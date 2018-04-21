## 一、开机启动

可以设置开机启动有两个地方：第一，在/etc/init.d目录下，可以将服务放到这个目录下。第二是在/etc/init.d下的rc.local，可以将需要开机启动的程序写入这个文件。可以使用sysv-rc-conf命令进行设置和查看开机启动服务。

- 在/etc/init.d/下新建一个脚本test，格式如下：

  ~~~
  #!/bin/bash

  #要执行的命令
  exit 0
  ~~~

- 增加脚本可执行权限


  ~~~
sudo chmod +x test
  ~~~
- 设置开机启动

  ~~~
  sudo update-rc.d test defaults 90  #90是优先级，越大优先级越低，越晚执行
  ~~~
- 使用sysv-rc-conf命令设置运行级别

  ~~~
  #sysv-rc-conf默认没有安装，首先安装
  sudo apt-get install sysv-rc-conf

  #执行命令sysv-rc-conf，用空格键选中或取消指定的运行级别。

  #取消开机启动可以使用
  sudo update-rc.d -f 脚本名  remove
  ~~~


## 二、防火墙

UFW或Uncomplicated Firewall是iptables的接口，旨在简化配置防火墙的过程。UFW默认安装在Ubuntu上。如果没有安装，你可以使用sudo apt-get install ufw 。

- ufw常见操作

  ~~~
  sudo ufw status                 #查看状态和规则
  sudo ufw disable                #禁用
  sudo ufw enable                 #启用
  sudo ufw reset                  #重置
  sudo ufw status numbered        #显示规则编号
  ~~~

- 设置默认策略

  如果您刚刚开始使用防火墙，则首先要定义的规则是您的默认策略。这些规则控制如何处理未明确匹配任何其他规则的流量。

  ~~~
  sudo ufw default deny incoming   #拒绝所有传入连接
  sudo ufw default allow outgoing  #允许所有传出连接
  ~~~

- 开启或禁用指定连接

  ~~~
  #允许连接
  sudo ufw allow 端口/服务

  #允许ssh远程连接
  sudo ufw allow ssh  #或者sudo ufw allow 22/tcp  

  #允许未加密的web访问
  sudo ufw allow http  #或sudo ufw allow 80
  #允许加密的web访问
  sudo ufw allow https  #或sudo ufw allow 443

  #允许ftp访问
  sudo ufw allow ftp  #或sudo ufw allow 21/tcp

  #允许远程mysql访问
  sudo ufw allow 3306

  #允许特定范围的端口
  sudo ufw allow 6000:6007/tcp #允许使用端口6000 - 6007 X11连接

  #允许特定ip地址
  sudo ufw allow from 15.15.15.51

  #允许特定子网
  sudo ufw allow from 15.15.15.0/24  #允许所有的IP地址范围从15.15.15.1到15.15.15.254

  #拒绝连接
  sudo ufw deny http
  sudo ufw deny from 15.15.15.51
  ~~~

- 删除规则

  ~~~
  sudo ufw status numbered #先查看编号
  sudo ufw delete 2  #再按编号删除

  #按实际规则
  sudo ufw delete allow http
  sudo ufw delete allow 80
  ~~~

  ​
