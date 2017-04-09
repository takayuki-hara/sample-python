#! /usr/bin/env python
# coding: utf-8
#-----------------------------------------------------------
# @file		extract_log.py
# @brief	ログファイル群から所定のものを抽出する
# @date		2017/04/08
# @author	takayuki-hara
# @usage	所定のファイル構成において本スクリプトを実行する
#-----------------------------------------------------------

import os

# 定数定義
TARGET_DIRS = [ 'log1',  'log2',  'log3', ]
INPUT_FILE  = 'log.txt'
OUTPUT_DIR  = 'output'
OUTPUT_LOG  = 'output.txt'


def extract_log(file_path, target):
	in_file = open(file_path, 'r')
	out_file = open(os.path.join(os.getcwd(), OUTPUT_DIR, '%s-%s' % (target, OUTPUT_LOG)), 'w')
	for line in in_file:
		if 'Salem Version:' in line:
			out_file.write(line)
	in_file.close()
	out_file.close()


# main関数
def main():
	os.mkdir(OUTPUT_DIR)
	for target in TARGET_DIRS:
		file_path = os.path.join(os.getcwd(), target, INPUT_FILE)
		extract_log(file_path, target)


if __name__ == '__main__':
	main()
