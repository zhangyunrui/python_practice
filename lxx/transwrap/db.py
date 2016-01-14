# -*- coding: utf-8 -*-
import datetime
import threading


class _Engine(object):
    def __init__(self, connect):
        self._connect = connect
    def connect(self):
        return self._connect()

# e = _Engine(datetime.datetime.now)
# print e.connect()

engine = None

class _DbCtx(threading.local):
    pass