def power(x):
    return x * x;

print("power(5) =", power(5))
print("power(15) =", power(15))

def power(x, n=2):
    s = 1
    while n > 0:
        s *= x
        n -= 1
    return s
print("power(5, 2) =", power(5, 2))
print("power(5, 3) =", power(5, 3))
print("power(5) =", power(5))

def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)
enroll('Sarah', 'F')

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
enroll('Sarah', 'F')

# def add_end(L=[]):
def add_end(L=None):
    if(L is None):
        L = []
    L.append('END')
    return L
print('add_end([1, 2, 3])=', add_end([1, 2, 3]))
print('add_end([\'x\', \'y\', \'z\'])=', add_end(['x', 'y', 'z']))
print('add_end()=', add_end())
print('add_end()=', add_end())

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum
print('calc(1, 2) =', calc(1, 2))
print('calc() =', calc())

nums = [1, 2, 3]
print('calc(nums) =', calc(*nums))

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Mochael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
