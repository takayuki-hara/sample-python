#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------
# @file     divide_file.py
# @brief    特定の文字を含む行とそうでない行を別のファイルに分割する
#           ※リストアップされたファイルから対象外の文字列を含むものを除去したい
# @date     2017/04/08
# @author   takayuki-hara
# @usage    作業ディレクトリにこのスクリプトと"input.txt"を配置して実行する
#-----------------------------------------------------------

import os


# ファイル
INPUT_FILE = 'input.txt'
OUTPUT_INCLUDE_FILE = 'include_specify_string.txt'
OUTPUT_EXCLUDE_FILE = 'exclude_specify_string.txt'


# メイン
def main():
    in_file = open(INPUT_FILE, 'r')
    out_in_file = open(OUTPUT_INCLUDE_FILE, 'w')
    out_ex_file = open(OUTPUT_EXCLUDE_FILE, 'w')

    for line in in_file:
        if 'cocoapods' in line:
            out_in_file.write(line)
        else:
            out_ex_file.write(line)
    in_file.close()
    out_in_file.close()
    out_ex_file.close()


if __name__ == '__main__':
    main()
