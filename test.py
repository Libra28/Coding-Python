# -*- coding: utf-8 -*
"""
获取指定商品设置和取消折扣URL
"""
import requests,json,time
from get_token import get_file_token
from cate_items import cate_items

cate_id = 81018763
discount = 0.38
access_token = get_file_token()
items = cate_items(str(cate_id))


"""
url = 'https://api.vdian.com/api?param={"itemid":"%d","price":"%.1f","quantity":"999999","start_time":"2016-06-2 15:23:00","end_time":"2016-06-27 14:58:00"}&public={"method":"vdian.seckill.item.set","access_token":"%s","version":"1.0","format":"json"}' % (itemid,price,access_token)

print url

url1 = 'https://api.vdian.com/api?param={"itemid":"%d"}&public={"method":"vdian.seckill.item.delete","access_token":"%s","version":"1.0","format":"json"}' % (itemid,access_token)

print url1
"""

https://api.vdian.com/api?param={"itemid":"1865348296"}&public={"method":"vdian.seckill.item.delete","access_token":"9de9530574e8ac3ca20ee522bcf2342e00048975ec","version":"1.0","format":"json"}
