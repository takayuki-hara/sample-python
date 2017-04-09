#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------
# @file     get_file.py
# @brief    入力ファイルに記述されている追加音声をTTSサーバーから取得する
# @date     2017/04/08
# @author   takayuki-hara
# @usage    作業ディレクトリにこのスクリプトを配置して実行する
#-----------------------------------------------------------

import os
import urllib2
import codecs


# 通信パラメータ
URL = 'http://img01.ecgo.jp/usr/hispot-corp/img/topimage.png'


# HTTPリクエストを行う（通信結果を返す）
def http_request(url):
    res = urllib2.urlopen(url)
    return res.read()


# メディアファイルを取得して保存する
def get_file():
    data = http_request(URL)
    if data != None:
        image_file = open('image.jpg', 'wb')
        image_file.write(data)
        image_file.close()


# メイン
def main():
    get_file()

   
if __name__ == '__main__':
    main()
