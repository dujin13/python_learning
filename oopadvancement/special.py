class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

    def __getattr__(self, item):
        if item=='score':
            return 99
        if item == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)

    def __call__(self):
        print('My name is %s.' % self.name)

print(Student('Michael'))
s = Student('Michael')
print('s.name = ', s.name)
print('s.score = ', s.score)
print('s.age() = ', s.age())
# s.abc
s()

print('callable(Student()) =', callable(Student('Michael')))
print('callable(max) =', callable(max))
print('callable([1, 2, 3]) =', callable([1, 2, 3]))
print('callable(None) =', callable(None))
print('callable(\'str\') =', callable('str'))

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

for n in Fib():
    print(n)

f = Fib()
print('f[0] =', f[0])
print('f[1] =', f[1])
print('f[2] =', f[2])
print('f[3] =', f[3])
print('f[10] =', f[10])
print('f[100] =', f[100])

print('f[0:5] =', f[0:5])
print('f[0:10] =', f[0:10])

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print('Chain().status.user.timeline.list =', Chain().status.user.timeline.list)