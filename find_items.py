# -*- coding: utf-8 -*
"""
获取分类商品
"""
import json,pickle

def find_items(item_id):
    global count
    count = 0
    items = []
    with open('items.txt','rb') as file:
        for i in range(1,9):
            r = pickle.load(file)
            for key in r:
                if key['item_name'] == item_id:
                    item = (key['itemid'],key['price'])
                    items.append(item)
                    count += 1
    return items

if __name__ == '__main__':
    i = find_items('81018763')
    print count,i[0]
