#!/usr/bin/env python3
import json
import os
import shelve
# import sys
# import PyQt5
# import sqlite3


def main():
    path = os.getcwd() + '\\data_base\\'
    os.mkdir(path)

    tariffs = {}
    with open('beta_tariffs.json') as f_tariffs:
        for name_tariff, describe_tariff in json.load(f_tariffs).items():
            tariffs[name_tariff] = Tariff(describe_tariff)

    users = {}
    for log in open('log.txt').readline():
        if log[3] is 'registration':
            if log[0] in users: raise Exception('repeated registration')
            users[log[0]] = User(log, tariffs)

        users[log[0]].action(log, tariffs)
        users[log[0]].add_history(log[1:])
        
        with shelve.open(data) as data_base:
            data_base[log[0]]


def determine_range_action(where, to):
    """determine condition for roaming"""
    where, to = where.split('_'), to.split('_')
    k = 0
    while len(to) > k and where[k] != to[k]: k += 1
    return k


class User(object):
    """Class for user PBX"""
    def __init__(self, log, tariffs):
        self.number = log[0]
        self.balance = 0
        self.history = []
        self.package = tariffs[log[4]]['packages'].copy()
        self.name_tariff = log[3]
        if not tariffs[log[4]].dynamic_position:
            self.position = log[2]

    def add_history(self, history):
        pass

    def action(self, log, tariffs):
        if not log[3] in tariffs['action']: # существует ли это действие
            raise Exception(f'No this action {log[3]}')
        
        if log[3] in self.package:  # существует ли это действие в пакете
            # range_action = determine_range_action(log[2], log[5])
            # if tariffs[self.name_tariff].action[log[2]]
        else:
            pass


class Tariff(object):
    """Class for simple work with tariffs"""
    def __init__(self, tariffs):
        self.price = tariffs['price']
        self.dynamic_position = tariffs['dynamic_position']
        self.packages = tariffs['packages']
        self.action = tariffs['action']

    def change_parametr(self, parametr):
        d = {
            'price': self.price = parametr,
            'dynamic_position': self.dynamic_position = parametr,
            'packages': self.packages = parametr,
            'action': self.packages = parametr
        }
        d[parametr]


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
    
    hasattr(t, 'c') - проверить есть ли атрибут c
"""
