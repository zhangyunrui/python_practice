# -*- coding: utf-8 -*-
# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j*j
            return g
        fs.append(f(i))
    return fs

def count1():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

for fn in [(lambda j = i: j * j)for i in range(1, 4)]:
    print fn()

for fn in [(lambda : i * i)for i in range(1, 4)]:
    print fn()

for fn in count():
    print fn()

for fn in count1():
    print fn()