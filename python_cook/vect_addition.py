# -*- coding: utf-8 -*-
class Vector(object):
    def __init__(self, x, y):
        self.vec_repr = x, y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __getattr__(self, name):
        if name == "x":
            return self.vec_repr[0]
        elif name == "y":
            return self.vec_repr[1]

a = Vector(1, 1)
b = Vector(2, 2)
c = a + b
print a.vec_repr
print c.vec_repr
