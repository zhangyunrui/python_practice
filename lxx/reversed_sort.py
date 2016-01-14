# -*- coding: utf-8 -*-
print sorted([36, 5, 12, 9, 21])

def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

print sorted([36, 5, 12, 9, 21], reversed_cmp)
print sorted([36, 5, 12, 9, 21], lambda x, y: y - x)
