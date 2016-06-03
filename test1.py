# -*- coding: utf-8 -*
"""
获取指定商品名称
"""
import pickle


def get_name(itemid):
    with open('items.txt', 'rb') as file:
        for i in range(1, 9):
            r = pickle.load(file)
            for key in r:
                if key['itemid'] == itemid:
                    return key['item_desc'].encode('gb2312')
                    break


itemid = '1865347194'
print get_name(itemid)
"""
1865347191

{"status":{"status_code":10008,"status_reason":"非法请求(这个商品已经创建折扣了-2) "}}
1865347192

{"status":{"status_code":10008,"status_reason":"非法请求(这个商品已经创建折扣了-2) "}}
1865347194

{"status":{"status_code":10008,"status_reason":"非法请求(这个商品已经创建折扣了-2) "}}
[Finished in 229.3s]
"""
