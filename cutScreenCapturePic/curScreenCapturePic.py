# coding=utf-8
"""
Problem: When screen capture for 2 display screens, there always one screen pic for use.
WhatToDo: cut-off the screen capture pic for only one screen.
Problem Sample:
Base Logic:
    Use image grab api to grab right size pic from right position, then save it.
Keyword arguments:
Return: nothing
"""

import os
from PIL import Image


def main():

  src_dir = r'D:\OneDrive\图片\屏幕快照\z.arch\2020-12-22_准备DevOps课程PPT'
  src_files = os.listdir(src_dir)

  idx = 1
  for src_file in src_files:
    fullpath = os.path.join(src_dir, src_file)
    if os.path.isfile(fullpath):

      img = Image.open(fullpath)

      (src_file_name, src_file_ext) = os.path.splitext(src_file)

      # 切去右边，留左边,目录：_去右留左
      # cropped = img.crop((4145, 142, 6137, 1436)) # 切小了
      cropped = img.crop((3990, 170, 6220, 1441))
      save_file_name = src_file_name + '_去右留左' + src_file_ext
      save_dir = r'D:\OneDrive\图片\屏幕快照\z.arch\2020-12-22_准备DevOps课程PPT\_去右留左'
      save_file_fullpath = os.path.join(save_dir, save_file_name)
      cropped.save(save_file_fullpath)
      cropped.close()

      # 切去左边，留右边,目录：_去左留右
      # cropped = img.crop((373, 403, 3133, 1855))
      # save_file_name = src_file_name + '_去左留右' + src_file_ext
      # save_dir = r'D:\OneDrive\图片\屏幕快照\z.arch\2020-12-22_准备DevOps课程PPT\_去左留右'
      # save_file_fullpath = os.path.join(save_dir, save_file_name)
      # cropped.save(save_file_fullpath)
      # cropped.close()

      img.close()
    else:
      pass

if __name__ == '__main__':
    main()