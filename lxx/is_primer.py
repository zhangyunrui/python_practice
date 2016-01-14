# -*- coding: utf-8 -*-
def is_primer(n):
    if not (n == 0 or n == 1):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


print filter(is_primer, range(100))

print [n for n in range(100) if not ([i for i in range(2, n) if n % i == 0] or n == 0 or n == 1)]
