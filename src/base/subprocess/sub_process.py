#! /usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------
# @file		sub_process.py
# @brief	シェルの呼び出しのサンプル
# @date		2017/04/08
# @author	takayuki-hara
# @usage	作業ディレクトリでこのスクリプトを実行する
#-----------------------------------------------------------

import subprocess


# 実行するコマンド	※この例ではXcodeがインストールされている前提
def command():
	try:
		cmd = 'xcode-select -p'
		cmd_list = cmd.strip().split(" ")
		subprocess.check_call(cmd_list)
	except Exception, e:
		raise


# メイン関数
def main():
	try:
		command()
	except Exception, e:
		print('error!')
	else:
		print('success!')


if __name__ == '__main__':
	main()

