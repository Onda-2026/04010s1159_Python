#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
プログラミング基礎Python
制御構文
練習問題6
P.13「continue文」のソースコードを以下に変更してください。
    numが奇数の場合、次の処理に移る。

静的解析ツール
================
================

実行例
================
>>> python SO203_05_Q6.py
2
4
================

'''


# ここより下に解答を記載する。
list_num=[1,2,3,4]

for num in list_num:
    if num % 2 == 1:
        continue
    print(num)
