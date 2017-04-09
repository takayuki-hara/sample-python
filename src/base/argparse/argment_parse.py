#! /usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------
# @file		argment_parse.py
# @brief	引数を設定するサンプル
# @date		2017/04/08
# @author	takayuki-hara
# @usage	作業ディレクトリでこのスクリプトを実行する
# @note		参考：https://docs.python.jp/3/library/argparse.html
#-----------------------------------------------------------

import os
import argparse


# メイン関数
def main():
	parser = argparse.ArgumentParser(description='Sample ArgmentParser.')

	# オプション引数："-vvv"とかvの数でログレベルを指定させる
	parser.add_argument('--verbose', '-v', action='count')
	# 位置引数："config Debug"とかでconfigurationを指定させる
	parser.add_argument('config', action='store', nargs=None, const=None, default='Release', type=str, choices=['Release','Debug'], help='build configuration', metavar='config')

	args = parser.parse_args()
	print(args.verbose)
	print(args.config)


if __name__ == '__main__':
	main()

