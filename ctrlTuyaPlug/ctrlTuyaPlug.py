# -*- coding: utf-8 -*-
"""
  checkBattery.py
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Cause the HP Envy15 AS110-tu has no strategy to protect battery for over charging, liking other band laptop, such as DELL.
  For example: DELL laptop will stop charging when battery volume reaches 95%.

  This program is to warning user to unplug power with battery volume reaches 85%, and plug the battery when battery volume left 35%.

  The warning will be Beep sound, and Message box pop up.

  参考： https://www.mdeditor.tw/pl/gbyF

  :copyright: (c) 2020/11/06 by wanglei.
  :license: MIT

TODO:
"""


# 从云开发项目获得的授权密钥
client_id = 'hmrjarqradeiou76xm51'
secret = '71cb7144d64b4517bedddf575005f1d0'

base = 'https://openapi.tuyacn.com'

# 签名算法函数
def calc_sign(msg,key):
  import hmac
  import hashlib

  sign = hmac.new(msg=bytes(msg, 'latin-1'),key = bytes(key, 'latin-1'), digestmod = hashlib.sha256).hexdigest().upper()
  return sign

import time
import requests

t = str(int(time.time()*1000))
r = requests.get(base+'/v1.0/token?grant_type=1',
                 headers={
                    'client_id':client_id,
                    'sign':calc_sign(client_id+t, secret),
                    'secret':secret,
                    't':t,
                    'sign_method':'HMAC-SHA256',
                  })

res = r.json()['result']
print(res)