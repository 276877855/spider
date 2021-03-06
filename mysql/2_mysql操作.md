# 数据库

## 一、数据库基本概念

数据的仓库

## 二、SQL

基本可分为：

- 数据定义语言DDL (create、drop）
- 数据操作语言DML（insert、delete、update）
- 数据查询语言DQL（select、where、group by、order by 、limit）
- 数据控制语言DCL（grant、revoke）
- 事务处理语言TPL（commit、rollback）



## 三、操作数据库

- 连接mysql数据库的命令

  ~~~
  命令：
      mysql -h服务器名 -u用户名  -p  #不要再p后面直接跟密码
  ~~~

- 数据库操作命令

  ~~~
  #1.查看库
     show databases;
  #2. 创建库
     create database 数据库名 default charset=utf8;# 数据库名不要纯数字，不要用汉字
  #3. 删除库
     drop database 数据库名;
  #4. 选中库
     use 数据库名;
  #5. 查看表
     show tables;
  ~~~

- 注意

  - 每条命令结束必须使用; 或者 \g 结束
  - 退出mysql使用命令quit或exit


## 四、数据库表

- 创建表

  ~~~
  create table [if not exists] 表名(
     列名1  类型  [限制],
     列名2  类型  [限制],
     ...
     列名n  类型  [限制]  #最后一列没有逗号
  ) [engine=myisam | innodb][ default charset=utf8];

  primary key 主键 不允许有重复值
  auto_increment 自增长，只对int型主键起作用
  ~~~

- 删除表

  ~~~
  drop table 表名;
  ~~~

- 查看表结构

  ~~~
  desc 表名;
  ~~~

- 查看建表语句

  ~~~
  show create table 表名;
  ~~~

- 修改表

  ~~~
  #修改字段类型
     alter table 表名 modify 字段名 类型 [限制]
  #增加字段
     alter table 表名  add [column] 字段名 类型 [限制];
  #删除字段
     alter table 表名 drop [column] 字段名;
  修改字段名和类型
     alter table 表名 change [column] 旧字段名 新字段名 类型 [限制];
     
  #修改表名
    alter table 表名 rename 新表名
  ~~~

- 字段限制

  ~~~
  not  null 非空
  unique 唯一
  default  缺省
  ~~~

## 五、数据类型

- 数值型

  - 整型 能用整型尽量使用整型。包括int、smallint  tinyint
  - 浮点数  double 、decimal

- 字符型

  - char(长度)  定长字符串   0-255字符 
  - varchar(长度)  变长字符串  0-65535字符

- 日期时间型

  - datetime  输入的时候用字符串 '2018-3-27 3:00:00'
  - date

- 枚举enum

  ~~~
  #是自定义类型，可以多选一,实际上存的值是1，2，3...
  alter table user add sex enum('男','女') default '男';
  insert into user(name,password,sex) 
  values('tom','132','男');
  values('tom','132',1);
  ~~~

- 集合set

  ~~~
  类似复选框，可以存多个值
  insert into users(uid,hobby) values(22,1+2+4+8)
  insert into users(uid,hobby) values(22,1|2|4|8)
  insert into users(uid,hobby) values(22,'足球,篮球,桌球')
  ~~~

  ​

##六、数据操作

### 1. insert

  ~~~
写法一：insert into 表名(字段1，字段2...) values(值1,值2...);

省略了字段列表，则按照建表时的字段顺序进行插入，每一列都要给值
写法二：insert into 表名 values(值1,值2...);
写法三：插入多个记录
	   insert into 表名(字段1，字段2...) 
			 values(值1,值2...),
			 (值1,值2...),
			 (值1,值2...)....
写法四： insert into 表名(name,age,sex)
		select name,age,sex from stars;
  ~~~

### 2.update

~~~
 update 表名 set 字段1=值1,字段2=值2... where 条件  #不加where修改的是所有的记录
~~~

### 3. delete

~~~
删除表中的数据，自增主键的值不会重新开始
delete from 表名 where 条件；#如果不加条件，会删除表中所有数据,慎重使用

清空表，自增主键的值重新开始编号
truncate 
	   truncate table 表名,清空表中所有记录，等价于delete from 表名；
	   delete和truncate差别，truncate后，表中自增主键值从1开始
~~~

## 七、数据查询

基本结构： select  字段名列表   from 表名

### 1 基础查询

~~~~
select username,password  from user;
select usernname as 用户名, password as 密码  from user;  #可以给字段起别名
select *  from user; #查询所有字段，慎用，一般不建议使用，会导致无法优化sql语句
select 2018,username,password  from user; #可以有常量，表达式
select distinct username  from  user; #去除重复记录 distinct 针对查询结果去除重复记录，不针对字段
~~~~

###2 条件查询（where） 

- 关系运算

  关系运算符：> 、 >=、  <、  <=、  =、!=、<>、 between and

  ~~~
  select username,password from user where uid <10
  select username,password from user where uid != 10
  select username,password from user where uid between 10 and 20
  ~~~

- 逻辑运算

  逻辑运算符：and 、or、not

  ~~~
  select username,password from user where uid < 100 and uid > 20;
  select username,password from user where uid > 100 or uid < 20;
  ~~~

- 集合运算

  集合运算符：in、not in

  ~~~
  select username,password form user where uid in (2,3,4)
  select username,password form user where uid not in (2,3,4)
  ~~~

- 判空

  判空运算：is  null、is not  null

  ~~~
  select username,password from user where username is null
  ~~~

- 模糊查询(like)

  通配符 _代表一个字符，%代表任意长度字符串

  	select * from user where username like '王_';
  	select * from user where username like '王%';

### 3. 排序（order by）

 asc 升序(默认)、desc  降序、

	select * from user order by age asc;
	select * from user order by age desc;
	多字段排序
	   	select name,age from php_user_history  order by age desc,name;# 如果在第一列上有相同的值，在具有相同的age的记录上再按name升序排列
### 4.限制结果集(limit)

limit n    #取前n条记录

limit  offset,n #从第offset条开始取，取n条

	select * from php_user_history limit 3;
	select * from php_user_history limit 4,2;
	注意结果集中记录从0开始数数，offset相对于0开始
	实现分页必须的技术点
### 5.集合函数

- count统计结果集中记录数
- max 最大值
- min  最小值
- avg   平均值，只针对数值类型统计
- sum 求和，只针对数值类型统计
- 注意，集合函数不能直接使用在where后面的条件里，但可以在子查询中

 ~~~
select count(*) num from user;
select count(distinct age) num from user; //去除重复记录
 ~~~

### 分组（group by)

将结果集分组统计，规则：

- 出现了groub by的查询语句，select后面的字段只能是集合函数和group by后面有的字段，不要跟其它字段
- 对分组进行过滤，可以使用having

~~~
select uid, count(*) num from php_forum group by uid;
select uid,title, count(*) num from forum group by uid having count(*) >=2;
~~~

### 查询小结

- 整体顺序不能颠倒
- []表示可选，可以有也可以没有

   select 字段
    from 表名
     [where 条件]
     [group by ]
     [having]
     [order by ]
     [limit]	 

## 8 字符集和存储引擎

- 修改字符集

为了能够正常显示中文，必须把数据库的字符集设置为utf8.

~~~
mysql> show variables like 'character%';  #查看字符集
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | utf8                       |
| character_set_connection | utf8                       |
| character_set_database   | latin1                     |需要修改
| character_set_filesystem | binary                     |
| character_set_results    | utf8                       |
| character_set_server     | latin1                     |需要修改
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+
8 rows in set (0.01 sec)

修改mysql的配置文件
cd /etc/mysql/mysql.conf.d
sudo cp mysql.cnf  mysql.cnf.bak
sudo vim mysql.cnf
在[mysqld]下增加一句：
character_set_server = utf8
保存并重启服务
sudo systemctl restart mysql.service  #重启服务

~~~

- 数据库引擎
  - 常用的数据库引擎：myisam、innodb、archive、ndb、memory 
  - myisam和innodb的区别





+------------------+-------------------------------------------+
| root             | *AC41577E1541CD7EDB3598E6638EFBE23E4C0264 |
| mysql.session    | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
| mysql.sys        | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
| debian-sys-maint | *1BACBCD2E33134166F919F94011B1ACEC16D2686 |
+------------------+-------------------------------------------+