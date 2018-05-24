print("range(1, 11) =", list(range(1, 11)))
print("[x for x in range(1, 11)] =", [x for x in range(1, 11)])
print("[x * x for x in range(1, 11)] =", [x * x for x in range(1, 11)])
print("[x * x for x in range(1, 11) if x % 2 == 0] =", [x * x for x in range(1, 11) if x % 2 == 0])
print("[m + n for m in 'ABC' for n in 'XYZ'] =", [m + n for m in 'ABC' for n in 'XYZ'])

import os
print("[d for d in os.listdir('.')] =", [d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print("[k + '=' + v for k, v in d.items()] =", [k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print("[s.lower() for s in L] =", [s.lower() for s in L])