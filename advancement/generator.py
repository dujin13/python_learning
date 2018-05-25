g = (x * x for x in range(10))
print("g =", g)
for n in g:
    print("g.next() =", n)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(6)

def fibGenerator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
for n in fibGenerator(6):
    print("fibGenerator.next() =", n)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
for n in odd():
    print("odd.next() =", n)

g = fibGenerator(6)
while True:
    try:
        x = next(g)
        print('g =', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
