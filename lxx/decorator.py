# -*- coding: utf-8 -*-
from datetime import datetime
import functools


# Define the decorator without parameter
def log(func):
    def wrapper(*args, **kw):
        print 'call %s()' % func.__name__
        return func(*args, **kw)
    return wrapper


# 3 ways to use decorator
@log
def now():
    print "use @log in the front " + str(datetime.now())

now()

def now():
    print "use now = log(now) in the back " + str(datetime.now())

now = log(now)

now()

def now():
    print "call log(now)() imediately " + str(datetime.now())

log(now)()


# Define the decorator with parameter
def log(para='call'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s()' % (para, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

# 2 situation and 3 ways to use decorator
@log()
def now():
    print "use @log() in the front " + str(datetime.now())

now()

@log('execute')
def now():
    print "use @log('execute') in the front " + str(datetime.now())

now()

def now():
    print "use now = log('use')(now) in the back " + str(datetime.now())

now = log('use')(now)

now()

def now():
    print "use log('operate')(now)() imediately " + str(datetime.now())

log('operate')(now)()


# The decorator can be used in "@log" and "@log('para')"
def log(para):
    if callable(para):
        @functools.wraps(para)
        def wrapper(*args, **kw):
            print '%s %s()' % ('call', para.__name__)
            return para(*args, **kw)
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print '%s %s()' % (para, func.__name__)
                return func(*args, **kw)
            return wrapper
        return decorator

# two ways to use decorator
@log
def now():
    print "first way of two ways " + str(datetime.now())

now()

@log('2_ways_call')
def now():
    print "second way of two ways " + str(datetime.now())

now()
