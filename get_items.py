# -*- coding: utf-8 -*
"""
获取全部商品
"""
import requests,json,pickle
from get_token import get_file_token
access_token = get_file_token()

with open('items.txt','wb') as file:
    for i in range(1,9):
        url = 'https://api.vdian.com/api?param={"page_num":%d,"page_size":200}&public={"method":"vdian.item.list.get","access_token":"%s","version":"1.0","format":"json"}' % (i,access_token)

        r = json.loads(requests.get(url).text)
        items = r['result']['items']
        pickle.dump(items,file)

