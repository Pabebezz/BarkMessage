#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：Pabebe
@Date   ：2020/8/28 21:15
@Description   ：
=================================================='''
# 确认当前所在目录 应该在BarkMessage的上一级
import os
if 'BarkMessage' in os.getcwd():
    os.chdir('D:/PyCharm 2020.1.2/workspace')
print(os.getcwd())

from configparser import ConfigParser
from .options import OptionsParser
from .PushMessage import Bark

if __name__ == '__main__':

    conf_path = './BarkMessage/default.ini'
    conf = ConfigParser()
    conf.read(conf_path, encoding='utf-8')
    print(dict(conf))
    conf_bark = conf['bark']
    op = OptionsParser()
    args = op.get_args()
    Bark(conf_bark['bark-url'], args.send)