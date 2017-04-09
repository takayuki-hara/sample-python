#! /usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------
# @file		class.py
# @brief	クラス定義のサンプル
# @date		2017/04/08
# @author	takayuki-hara
# @usage	作業ディレクトリでこのスクリプトを実行する
#-----------------------------------------------------------

import os
import sys


# パーソンクラス
class Person(object):
	def __init__(self, name, sex):
		self.name = name
		self.sex = sex


# パーソンクラスの集合のクラス
class Team(object):
	def __init__(self):
		self.initPersons()

	def initPersons(self):
		self.jon     = Person('jon', '')
		self.alice   = Person('alice', '')
		self.persons = [self.jon, self.alice]


# メイン関数
def main():
	tom = Person('tom', 'man')
	print(tom.name)
	
	team = Team()
	for person in team.persons:
		print(person.name)


if __name__ == '__main__':
	main()

