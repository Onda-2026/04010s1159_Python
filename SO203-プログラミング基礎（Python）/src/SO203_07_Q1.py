#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
プログラミング基礎Python
クラスとインスタンス
練習問題1
P.9～10「クラス」の学生クラスを拡張して、以下の文言も表示してください。
    私の好きな教科は〇〇です。
※〇〇は、以下としてください。
    山田：国語
    田中：数学

静的解析ツール
================
================

実行例
================
>>> python SO203_07_Q1.py
私の名前は山田です。
A高校の野球部に入っています。
私の好きな教科は国語です。

私の名前は田中です。
A高校のテニス部に入っています。
私の好きな教科は数学です。

私の名前は山田です。
B高校の野球部に入っています。
私の好きな教科は国語です。

私の名前は田中です。
B高校のテニス部に入っています。
私の好きな教科は数学です。

================

'''


# ここより下に解答を記載する。
class Student:
    # クラス変数の定義
    school = 'A高校'

    # コンストラクタの定義
    def __init__(self, name, club, subject):
        # インスタンス変数の定義
        self.name = name
        self.club = club
        self.subject = subject

    # メソッドの定義
    def introduce(self):
        text = f'私の名前は{self.name}です。\n'
        text += f'{self.school}の{self.club}に入っています。\n'
        text += f'私の好きな教科は{self.subject}です。\n'
        return text


# インスタンス化
yamada = Student('山田', '野球部', '国語')
tanaka = Student('田中', 'テニス部', '数学')

# メソッドの呼び出し
print(yamada.introduce())
print(tanaka.introduce())

# クラス変数の再設定
Student.school = 'B高校'

# メソッドの呼び出し
print(yamada.introduce())
print(tanaka.introduce())
