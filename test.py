# -*- coding: utf-8 -*-
import os
import web
import time
import requests,json

def exprise_token():
    return true if time.time() - creat_time > expire_in else false

def get_token():
    grant_type = 'client_credential'
    appkey = '658077'
    secret = '9a8f69ba222e7e0afc97d27e7c78ec26'

    weidian_url = 'https://api.vdian.com/token?grant_type=%s&appkey=%s&secret=%s' % (grant_type,appkey,secret)

    r = json.loads(requests.get(weidian_url).text)
    return r

    access_token = r['result']['access_token']
    expire_in = r['result']['expire_in']
    creat_time = time.time()


get_token()

print exprise_token()

