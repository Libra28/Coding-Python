#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-02 20:37:16
# @Author  : Libra (69066656@qq.com)
# @Link    : https://github.com/Libra28
import csv

with open('1.csv', newline='', encoding='utf-16') as csvfile1:
    a = 0
    line = [csvfile1.readline()]
    with open('2.csv', 'w', newline='', encoding='utf-16') as csvfile2:
        writer = csv.writer(csvfile2, delimiter='\t')
        writer.writerow(line)
        reader = csv.DictReader(csvfile1, delimiter='\t')
        for row in reader:
            if a == 0:
                fieldnames = (list(row.keys()))
                writer = csv.DictWriter(
                    csvfile2, fieldnames=fieldnames, delimiter='\t')
                writer.writeheader()
                writer.writerow(row)
            else:
                row['newprepay'] = 0
                row['has_invoice'] = 0
                row['has_warranty'] = 0
                row['sell_promise'] = 0
                row['buyareatype'] = 1
                row['global_stock_type'] = 2
                row['global_stock_country'] = '香港'
                writer.writerow(row)
            a += 1

print('Finish!')
