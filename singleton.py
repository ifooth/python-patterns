#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class Account(Singleton):
    pass


class Test(Singleton):
    pass


if __name__ == '__main__':
    a = Account()
    b = Account()
    c = Test()
    d = Test()
    print 'a: %s\r\nb: %s\r\nc: %s\r\nd: %s' % (a, b, c, d)
