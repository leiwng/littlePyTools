# -*- coding: utf-8 -*-
"""
  checkBattery.py
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Cause the HP Envy15 AS110-tu has no strategy to protect battery for over charging, liking other band laptop, such as DELL.
  For example: DELL laptop will stop charging when battery volume reaches 95%.

  This program is to warning user to unplug power with battery volume reaches 85%, and plug the battery when battery volume left 35%.

  The warning will be Beep sound, and Message box pop up.

  :copyright: (c) 2020/11/06 by wanglei.
  :license: MIT

TODO:
"""

import psutil
import winsound
import win32api, win32con


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

  if not plugged and percent < BAT_LCL:
    beep4plug()
    win32api.MessageBox(0, "请立即插入电源！", "警告",win32con.MB_ICONWARNING)

  if plugged and percent > BAT_UCL:
    beep4unplug()
    win32api.MessageBox(0, "请立即拔掉电源！", "警告",win32con.MB_ICONWARNING)


