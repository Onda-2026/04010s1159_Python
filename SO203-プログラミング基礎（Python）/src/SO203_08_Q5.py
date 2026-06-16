#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
プログラミング基礎Python
ファイル処理
練習問題5
P.16～17「CSVファイル」のソースコードを以下に変更してください。
    読み込むファイル名：SO203_08_Q5_input.csv
    書き出すファイル名：SO203_08_Q5_output.csv

静的解析ツール
================
================

実行例
================
>>> python SO203_08_Q5.py
>>> cat SO203_08_Q5_output.csv
リンゴ, 200, 3,600
オレンジ, 180, 2,360
バナナ, 120, 6,720
================

'''


# ここより下に解答を記載する。
import csv

# ファイルを開いて、csv読み込み用のストリームを取得する
file = open('SO203_08_Q5_input.csv', 'r')
csv_reader = csv.reader(file)

# 出力用の配列を用意する
out_data = []

# csvファイルを1行ずつ読み込む
for row in csv_reader:
    # 単価と個数から金額を計算する
    price = int(row[1]) * int(row[2])
    row.append(price)
    out_data.append(row)

file.close()

# ファイルを開いて、csv書き出し用のストリームを取得する
file = open('SO203_08_Q5_output.csv', 'w')
csv_writer = csv.writer(file, lineterminator='\n')

# csvファイルに書き出す
csv_writer.writerows(out_data)

file.close()
