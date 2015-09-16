#!/usr/bin/env python
# -*- coding=utf-8 -*-

__author__ = 'Caos'


# 测试专用
settings = {

    'userName': '',
    'password': '',
    'urls': 'http://weibo.com',
    'cookie_file': 'weibo_login_cookies.dat',
    'imageFlag': 'False',
    'fetchNum': '100'

}



class Config(dict):

    def __init__(self, names=(), values=(), **kw):
        super(self, Config).__init__(**kw)

        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise ArithmeticError(r"'Config' object has no attribute '%s' " % key)



    def __setattr__(self, key, value):
        self[key] = value
        
    def test_function():
        pass:

