# -*- coding: utf-8 -*
import json,pickle

count = 0

with open('items.txt','rb') as file:
    for i in range(1,9):
        r = pickle.load(file)
        for key in r:
            if key['itemid'] == '1865348296':
                print key['item_desc'].encode('gb2312')
        break

