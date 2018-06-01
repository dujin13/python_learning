print('int(\'12345\') =', int('12345'))
print('int(\'12345\', base=2) =', int('12345', base=8))

import functools
int2 = functools.partial(int, base=2)

print('int2(\'1000000\') =', int2('1000000'))
print('int2(\'1010101\') =', int2('1010101'))

max2 = functools.partial(max, 10)
print('max2(5, 6, 7) =', max2(5, 6, 7))