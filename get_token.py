# -*- coding: utf-8 -*-
"""
获取access_token并写入token.txt
"""
import os,time,requests,json,pickle

def get_file_token():
    if os.path.exists('token.txt'):
        load_token()
        if exprise_token():
            write_token()
        else:
            pass
    else:
        write_token()

    return r['result']['access_token']

def write_token():
    global r
    r = get_token()
    with open('token.txt','wb') as file:
        pickle.dump(r,file)

def load_token():
    with open('token.txt','rb') as file:
        global r
        r = pickle.load(file)

def exprise_token():
    expire_in = r['result']['expire_in']
    if time.time() - os.path.getctime('token.txt') > expire_in - 600:
        True
    else:
        False

def get_token():
    grant_type = 'client_credential'
    appkey = '658077'
    secret = '9a8f69ba222e7e0afc97d27e7c78ec26'
    url = 'https://api.vdian.com/token?grant_type=%s&appkey=%s&secret=%s' % (grant_type,appkey,secret)
    return json.loads(requests.get(url).text)

if __name__ == '__main__':
    print get_file_token()
