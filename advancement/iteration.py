d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key, d[key])

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)

for ch in 'ABC':
    print(ch)

from collections import Iterable
print("isinstance('abc', Iterator) =", isinstance('abc', Iterable))
print("isinstance([1,2,3], Iterator) =", isinstance([1,2,3], Iterable))
print("isinstance(123, Iterator) =", isinstance(123, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)