#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-02 20:37:16
# @Author  : Libra (69066656@qq.com)
# @Link    : https://github.com/Libra28
import csv
import re
import os

a = 0

with open('1.csv', newline='', encoding='utf-16') as csvfile:
    csvfile.readline()
    reader = csv.DictReader(csvfile, delimiter='\t')
    for row in reader:
        a += 1
        if a > 1:
            old_name = re.search(r'contentPic/(.*)-1.jpg',
                                 row['description'], re.M | re.I).group(1)
            l = len(old_name)
            new_name = row['inputValues']
            for file in os.listdir("."):
                if file[0:l] == old_name:
                    os.rename(file, new_name + file[l:])
                    print(file, '->', new_name + file[l:])
