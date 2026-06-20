#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
プログラミング基礎Python
プログラミング演習
問題2
コマンドライン引数で指定する範囲の整数を表示してください。
ただし、3の倍数のときは数の代わりに「Fizz」を、5の倍数のときは「Buzz」を出力し、
3と5両方の倍数のときは「FizzBuzz」を出力すること。

静的解析ツール
================
================

実行例
================
>>> python SO203_09_Q2.py
コマンドライン引数が不正です。
================
>>> python SO203_09_Q2.py 1
コマンドライン引数が不正です。
================
>>> python SO203_09_Q2.py 1 15
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
================

'''


# ここより下に解答を記載する。
import sys

# コマンドライン引数の数を確認
if len(sys.argv) != 3:
    print('コマンドライン引数が不正です。')
else:
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    for num in range(start, end + 1):
        if num % 15 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)
