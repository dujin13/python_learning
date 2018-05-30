def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operend type')
    if x >= 0:
        return x
    else:
        return -x;

print("my_abs(-99) =", my_abs(-99))

from function.my_abs2 import my_abs2
print("my_abs2(-9) =", my_abs2(-9))

def nop():
    pass
nop()

# print("my_abs('a') =", my_abs('a'))

import math
def move(x, y, step, angel=0):
    nx = x + step * math.cos(angel)
    ny = y - step * math.sin(angel)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x,",", y)

r = move(100, 100, 60, math.pi / 6)
print("r =", r)