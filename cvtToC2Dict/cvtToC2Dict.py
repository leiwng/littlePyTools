# -*- coding: utf-8 -*-
"""
  cvtToC2Dict.py
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Convert ToC (Table of Content from Word document) text to List of Dict in Python

  Sample of Source file:

  1	宏观经济学	1
  1.1	商业银行理论	1
  1.1.1	银行存款准备金率的概念	1
  1.1.2	存款准备金率变动对商业银行的影响	1

  :copyright: (c) 2020/11/06 by wanglei.
  :license: MIT

TODO:
"""


if __name__ == "__main__":

  TOC = []

  with open('toc.txt') as file:

    for line in file:

      idx = 0
      for word in line.split(' '):
        if idx == 0:
          pass
        elif idx == 1:
          pass
        elif idx == 2:
          pass
        else:
          pass
        idx += 1


