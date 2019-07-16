#! /usr/bin/env python
# coding: utf-8
#-----------------------------------------------------------
# @file		line_sort.py
# @brief	ログファイル１行ずつ読み込み、カンマ区切りで分けてソートする
# @date		2019/07/16
# @author	takayuki-hara
# @usage	所定のファイル構成において本スクリプトを実行する
#-----------------------------------------------------------

import os

# 定数定義
INPUT_FILE  = 'input.txt'
OUTPUT_FILE  = 'output.txt'


def sort_line():
	in_file = open(INPUT_FILE, 'r')
	out_file = open(OUTPUT_FILE, 'w')
	for line in in_file:
		trim = line.replace('\n','')
		array = trim.split(",")
		array.sort()
		str = ','.join(array) + '\n'
		out_file.write(str)
	in_file.close()
	out_file.close()


# main関数
def main():
	sort_line()

if __name__ == '__main__':
	main()
