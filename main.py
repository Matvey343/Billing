#!/usr/bin/env python3
import json
# import os
# import shelve
# import sys
# import PyQt5
# import sqlite3


def main():
    # root_path = 'D:\\python\\test\\'
    with open('beta_tariffs.json') as f_tariffs:
        tariffs = {}
        for name_tariff, describe_tariff in json.load(f_tariffs).items():
            tariffs[name_tariff] = Tariff(describe_tariff)
    users = {}
    for log in open('log.txt').readline():
        if log[3] is 'registration':
            if log[0] in users: raise Exception('repeated registration')
            users[log[0]] = User(log)
        users[log[0]].action(log)

# def determine_range_action(from_which, to):
#     from_which, to = from_which.split(), to.split()
#     for i in range(from_which):
#         if from_which[i] == to[i]:
#             return i
#     raise Exception()


class User(object):
    """Class for user PBX"""

    def __init__(self, log):
        self.number = log[0]
        self.balance = 0
        self.history = []
        self.package = log[4]
        self.position = log[2]

        self.add_history(log[1:])

    def add_history(self, history):
        self.history.append(history)

    def action(self, log):
        if log[3] in self.package:  # есть ли это действие в пакете
            pass
        else:
            pass

    def change_balanse(self, tariffs, action, solution):
        pass


class Tariff(object):
    """Class for simple work with tariffs"""

    def __init__(self, tariffs):
        self.price = tariffs['price']
        self.dynamic_position = tariffs['dynamic_position']
        self.packages = tariffs['packages']
        self.activity = tariffs['activity']


if __name__ == '__main__':
    main()

""""
    os.getcwd() - текущая директория
    os.listdir('D:\\python\\test') - список файлов в директории
    os.mkdir('D:\\python\\test\\test_dir') - создание директории
    os.remove('D:\\python\\test\\Кострыкин(Алгем).pdf') - удаляем файл
    os.rmdir() - удаление пустой директории
    os.path.exists(filename) - существование файла
    
    raise Exception - восстановление
"""
