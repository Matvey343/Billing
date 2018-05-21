#!/usr/bin/env python3
import json
import os
import argparse
import shelve
import logging
import sys
import PyQt5
import sqlite3


def main():
    with open('tariffs.json') as f_tariffs:
        tariffs = json.load(f_tariffs)
        f_tariffs.close()
    path = 'D:\\python\\test\\'
    f_log = open('log.txt')
    line = f_log.readline().split()
    f_log.close()


if __name__ == '__main__':
    main()


""""
os.getcwd() - текущая директория
os.listdir('D:\\python\\test') - список файлов в директории
os.mkdir('D:\\python\\test\\test_dir') - создание директории
os.remove('D:\\python\\test\\Кострыкин(Алгем).pdf') - удаляем файл
os.rmdir() - удаление пустой директории
os.path.exists(filename) - существование файла

"""