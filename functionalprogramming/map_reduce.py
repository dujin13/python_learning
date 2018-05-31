def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print("list(r) =", list(r))

print("list(map(str, range(10)) =", list(map(str, range(10))))

from functools import reduce
def add(x, y):
    return x + y

print('reduce(add, range(10)) =', reduce(add, [x for x in range(10) if x%2 == 1]))

def fn(x, y):
    return x * 10 + y
print('reduce(fn, range(10)) =', reduce(fn, [x for x in range(10) if x%2 == 1]))

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print('reduce(fn, map(char2num, \'13579\')) =', reduce(fn, map(char2num, '13579')))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
print('str2int(\'13579\') =', str2int('13579'))

def char2num2(s):
    return DIGITS[s]
def str2int2(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num2, s))
print('str2int2(\'13579\') =', str2int2('13579'))