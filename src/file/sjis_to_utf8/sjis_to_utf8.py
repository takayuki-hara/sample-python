#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------
# @file     sjis_to_utf8.py
# @brief    Shft-Jisの入力ファイルをUTF-8変換して保存する
# @date     2017/04/08
# @author   takayuki-hara
# @usage    作業ディレクトリにこのスクリプトと"sample.txt"を配置して実行する
#-----------------------------------------------------------

import os
import codecs


# 入力ファイル（Shift-Jis）
INPUT_FILE = 'sample.txt'
UTF8_SUFFIX = '-utf8'


# Shft-Jisの入力ファイルをUTF-8変換して保存する
def shiftjis_to_utf8(file_name):
    fin = codecs.open(file_name, 'r', 'shift_jis')
    name, ext = os.path.splitext(file_name)
    fout = codecs.open(name + UTF8_SUFFIX + ext, 'w', 'utf-8')
    # ファイルから一行ずつ読み込み，ファイルに出力する
    for line in fin:
        fout.write(line)
    fin.close()
    fout.close()

# メイン
def main():
    shiftjis_to_utf8(INPUT_FILE)

   
if __name__ == '__main__':
    main()
