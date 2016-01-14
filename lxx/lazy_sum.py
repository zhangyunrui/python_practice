# -*- coding: utf-8 -*-
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

ff = lazy_sum(*[3, 3, 5, 7, 9])
f = lazy_sum
f1 = lazy_sum(*[3, 3, 5, 7, 9])
f2 = lazy_sum(*[3, 3, 5, 7, 9])
print "lazy_sum(*[1, 3, 5, 7, 9])"
print lazy_sum(*[1, 3, 5, 7, 9])
print "s(*[1, 3, 5, 7, 9])"
print f(*[1, 3, 5, 7, 9])
print "ff = lazy_sum(*[3, 3, 5, 7, 9])"
print "ff"
print ff
print "f1 = lazy_sum(*[3, 3, 5, 7, 9])"
print "f1"
print f1
print "f2 = lazy_sum(*[3, 3, 5, 7, 9])"
print "f2"
print f2
print "lazy_sum(*[1, 3, 5, 7, 9])"
print lazy_sum(*[1, 3, 5, 7, 9])
print f2