#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-03 21:56:35
# @Author  : Libra (69066656@qq.com)
# @Link    : https://github.com/Libra28

import re

s = '优美世界2016春夏新品短款针织开衫空调衫女15X1W013'.decode('utf-8')
rule = re.compile(ur'[\u4e00-\u9fa5]')  # [\u4e00-\u9fa5]匹配所有中文的正则
list = rule.split(s)

while '' in list:
    list.remove('')

print list
