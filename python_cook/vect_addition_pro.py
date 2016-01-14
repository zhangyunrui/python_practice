# -*- coding: utf-8 -*-
class Vector:
    def __init__(self, x, y):
        self.vec_repr = x, y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    @property
    def x(self):
        return self.vec_repr[0]

    @property
    def y(self):
        return self.vec_repr[1]

a = Vector(1, 1)
b = Vector(2, 2)
c = a + b
print a.vec_repr
print c.vec_repr
