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

import time
import requests
import json
import hmac
import hashlib
import psutil
import winsound
import win32api, win32con

import logging

#from icecream import ic
from datetime import datetime

BAT_LCL = 35
BAT_UCL = 75

# 从云开发项目获得的授权密钥
client_id = 'hmrjarqradeiou76xm51'
secret = '71cb7144d64b4517bedddf575005f1d0'

device_name = 'WiFi智能插座(升级版)'
device_id = '3110664824a16018b63f'
product_id = 'vrwtvl200jaeeujr'

base = 'https://openapi.tuyacn.com'
url = '/v1.0/devices/'+device_id+'/commands'


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='ctrlTuyaPlug.log', level=logging.INFO, format=LOG_FORMAT)

# time format for icecream
def time_format():
  return f'{datetime.now()}|> '


# config output func for icecream
def logging_info(s):
  logging.info(s)


# config prefix for icecream
# ic.configureOutput(prefix=time_format, includeContext=True, outputFunction=logging_info)


# 签名算法函数
def calc_sign(msg,key):
  sign = hmac.new(msg=bytes(msg, 'latin-1'),key = bytes(key, 'latin-1'), digestmod = hashlib.sha256).hexdigest().upper()
  return sign

def get_token() :
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

  return res

# get 请求函数
def GET(url, headers={}):

  t = str(int(time.time()*1000))
  default_par={
      'client_id':client_id,
      'access_token':res['access_token'],
      'sign':calc_sign(client_id+res['access_token']+t, secret),
      't':t,
      'sign_method':'HMAC-SHA256',
  }
  r = requests.get(base + url, headers=dict(default_par,**headers))

  r = json.dumps(r.json(), indent=2, ensure_ascii=False) # 美化request结果格式，方便打印查看
  return r

# post 请求函数
def POST(res, headers={}, body={}):
  t = str(int(time.time()*1000))

  default_par={
      'client_id':client_id,
      'access_token':res['access_token'],
      'sign':calc_sign(client_id+res['access_token']+t, secret),
      't':t,
      'sign_method':'HMAC-SHA256',
  }
  r = requests.post(base + url, headers=dict(default_par,**headers), data=json.dumps(body))

  # r = json.dumps(r.json(), indent=2, ensure_ascii=False) # 美化request结果格式，方便打印查看
  return r

def test(res) :
  body = { "commands": [{"code":"switch_1", "value": False}] }
  POST(res, {}, body)


if __name__ == "__main__":

  battery = psutil.sensors_battery()
  plugged = battery.power_plugged
  percent = battery.percent

  if (not plugged) and (percent < BAT_LCL):
    cnt = 0 # try 3 times
    while (cnt<3) and (not plugged) and (percent < BAT_LCL):
      body = { "commands": [{"code":"switch_1", "value": True}] }
      res = get_token()
      POST(res, {}, body)
      logging.info('Power_ON - 电量：'+str(percent)+' %')

      # get battery status again
      battery = psutil.sensors_battery()
      plugged = battery.power_plugged
      percent = battery.percent

      cnt += 1
      time.sleep(3)

  elif plugged and (percent > BAT_UCL):
    cnt = 0
    while (cnt<3) and plugged and (percent > BAT_UCL):
      body = { "commands": [{"code":"switch_1", "value": False}] }
      res = get_token()
      POST(res, {}, body)
      logging.info('Power_OFF - 电量：'+str(percent)+' %')

      # get battery status again
      battery = psutil.sensors_battery()
      plugged = battery.power_plugged
      percent = battery.percent

      cnt += 1
      time.sleep(3)

  else:
    if plugged:
      tmp_str = '通电状态'
    else:
      tmp_str = '断电状态'
    logging.info('DO_NOTHING - 电量：'+str(percent)+' %'+' - '+tmp_str)