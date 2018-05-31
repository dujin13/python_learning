print('abs(-10) =', abs(-10))
print("abs =", abs)
x = abs(-10)
print("x =", x)
f = abs
print("f =", f)
print("f(-10) =", f(-10))
def add(a, b, f):
    return f(a) + f(b);
print('add(-10, 5, abs) =', add(-10, 5, abs))