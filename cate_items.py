# -*- coding: utf-8 -*
"""
获取分类商品
"""
import json,pickle

def cate_items(cate_id):
    global count
    count = 0
    items = []
    with open('items.txt','rb') as file:
        for i in range(1,9):
            r = pickle.load(file)
            for key in r:
                if key['cates'][0]['cate_id'] == cate_id:
                    item = (key['itemid'],key['price'])
                    items.append(item)
                    count += 1
    return items

if __name__ == '__main__':
    i = cate_items('81018763')
    print count,i[0]
