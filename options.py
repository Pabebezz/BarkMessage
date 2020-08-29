#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：Pabebe
@Date   ：2020/8/28 19:59
@Description   ：命令行参数
=================================================='''
import argparse


class OptionsParser():
    def __init__(self):
        # 创建一个解析器,ArgumentParser 对象包含将命令行解析成 Python 数据类型所需的全部信息。
        self.parser = argparse.ArgumentParser(description='Push Message')
        # 添加参数
        # - 短选项（Unix风格） --长选项（GNU风格）
        # metavar元变量,用于help中显示预期参数的位置。
        self.parser.add_argument("-s", "--send", metavar="message", type=str, default='喝水了嘛？',
                                 help='send  the message to ipone')

    def get_args(self):
        args = self.parser.parse_args()
        return args
