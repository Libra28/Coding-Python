# -*- coding: utf-8 -*-
import csv
import re
import os

a=0
b=[]
with open('1.csv', newline='',encoding='utf-16') as csvfile:
    csvfile.readline()
    reader = csv.DictReader(csvfile, delimiter='\t')
    for row in reader:
        a+=1
        if a>1:
            name=row['title'][-8:]
            if name  not in b:
                b.append(name)
            else:
                print(name,'is exists!!!')
