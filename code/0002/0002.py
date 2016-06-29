#将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

#coding:utf-8

import pymysql
import b


con = pymysql.connect(host='127.0.0.1', port=3306,
                      user='root', passwd='root',
                      charset="utf8")
cur = con.cursor()
cur.execute("create database if not exists pythondb")
cur.execute("use pythondb")
cur.execute("create table if not exists code1(key1 TEXT)")
for x in range(200):
	cur.execute("insert into code1 values('"+b.generateKey(4)+"')")
con.commit()
cur.close()
con.close()