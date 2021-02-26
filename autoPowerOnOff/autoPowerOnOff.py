# -*- coding: utf-8 -*-
"""
  autoPowerOnOff.py
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Cause the HP Envy15 AS110-tu has no strategy to protect battery for over charging, liking other band laptop, such as DELL.
  For example: DELL laptop will stop charging when battery volume reaches 95%.

  This program is to check the laptop battery and send command to intelligent socket for power on or power off.

  :copyright: (c) 2020/12/31 by wanglei.
  :license: MIT

TODO:
"""


import os
import psutil
import winsound
# import win32api, win32con
from win10toast import ToastNotifier

BAT_LCL = 35
BAT_UCL = 85


def beep4plug():
  duration = 1000  # millisecond
  freq = 440  # Hz
  winsound.Beep(freq, duration)

def beep4unplug():
  duration = 1000  # millisecond
  freq = 840  # Hz
  winsound.Beep(freq, duration)


if __name__ == "__main__":

  battery = psutil.sensors_battery()
  plugged = battery.power_plugged
  percent = battery.percent

  n = ToastNotifier()

  ico_dir = r'D:\Prj\littlePyTools\batChkNotifier'
  plugin_ico ='plugin.ico'
  plugout_ico ='plugout.ico'

  if not plugged and percent < BAT_LCL:
    beep4plug()
    msg = '请立即插入电源！电量：{}%。'.format(percent)
    ico_path = os.path.join(ico_dir,plugin_ico)
    n.show_toast("警告", msg, duration=10, icon_path=ico_path)
    # win32api.MessageBox(0, msg, "警告",win32con.MB_ICONWARNING)
    # print('plugin')

  if plugged and percent > BAT_UCL:
    beep4unplug()
    msg = '请立即拔掉电源！电量：{}%。'.format(percent)
    ico_path = os.path.join(ico_dir,plugout_ico)
    n.show_toast("警告", msg, duration=10, icon_path=ico_path)
    # win32api.MessageBox(0, msg, "警告",win32con.MB_ICONWARNING)
    # print('plugout')
    # print(ico_path)
