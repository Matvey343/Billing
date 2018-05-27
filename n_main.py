# !/usr/bin/env python3
import json
import os
import shelve
import sys
import PyQt5
import sqlite3


def main():
    path = os.getcwd() + '\\data_base'
    os.mkdir(path)
    path += '\\data'

    tariffs = {}
    with open('beta_tariffs.json') as f_tariffs:
        for name_tariff, describe_tariff in json.load(f_tariffs).items():
            tariffs[name_tariff] = Tariff(describe_tariff)

    for log in open('log.txt').readline():
        log = log.splite()
        with shelve.open(path) as db:

        user = shelve.open(pathx+log[0]).values


class Tariff(object):
    """Class for simple work with tariff"""
    def __init__(self, tariff):
        self.price = tariff['price']
        self.dynamic_position = tariff['dynamic_position']
        self.packages = tariff['packages']
        self.action = tariff['action']


class User(object):
    pass