#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：Pabebe
@Date   ：2020/8/28 17:09
@Description   ：往ipone上推送消息
=================================================='''


import time
import urllib.request
# import http.client



class Bark():
    def __init__(self, bark_url, message=None):
        # 时间戳
        day = time.strftime('%Y-%m-%d %H:%M:%S ', time.localtime(time.time()))

        '''      
        URL 组成: 第一个部分是 key , 之后有三个匹配
        /:key/:body
        /:key/:title/:body
        /:key/:category/:title/:body
        title 推送标题 比 body 字号粗一点
        body 推送内容
        category 另外的功能占用的字段，还没开放 忽略就行
        post 请求 参数名也是上面这些
        '''
        str = bark_url + day + message
        print('原始bark-url: ', str)
        # url若包含中文就编码 ， unquote解码
        res = urllib.request.quote(str, safe=";/?:@&=+$,", encoding="utf-8")
        # print('编码后bark-url: ', res)
        req = urllib.request.urlopen(res)
        # print(req.read().decode('utf-8'))



