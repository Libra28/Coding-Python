# -*- coding: utf-8 -*
"""
获取全部商品
"""
import requests,json,sqlite3
from get_token import get_file_token
access_token = get_file_token()
url = 'https://api.vdian.com/api?param={"page_num":1,"page_size":200}&public={"method":"vdian.item.list.get","access_token":"%s","version":"1.0","format":"json"}' % access_token
# 连接到SQLite数据库，数据库文件是items.db
# 如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('items.db')
# 创建一个Cursor:
cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 继续执行一条SQL语句，插入一条记录:
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()



print url

