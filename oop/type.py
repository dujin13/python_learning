print('type(123) =', type(123))
print('type(\'123\') =', type('123'))
print('type(None) =', type(None))

class Animal:
    pass
a = Animal()
print('type(abs) =', type(abs))
print('type(a) =', type(a))

print('type(123)==type(456) :', type(123)==type(456))
print('type(123)==type(int) :', type(123)==int)
print('type(\'456\')==type(\'123\') :', type('456')==type('123'))
print('type(\'123\')==str :', type('123')==str)
print('type(123)==type(456) :', type(123)==type(456))
print('type(123)==type(\'456\') :', type(123)==type('456'))

import types
def fn():
    pass
print('type(fn)==types.FunctionType :', type(fn)==types.FunctionType)
print('type(abs)==types.BuiltinFunctionType :', type(abs)==types.BuiltinFunctionType)
print('type(lambda x: x)==types.LambdaType :', type(lambda x: x)==types.LambdaType)
print('type((x for x in range(10)))==types.GeneratorType :', type((x for x in range(10)))==types.GeneratorType)


class Animal(object):
    pass

class Dog(Animal):
    pass

class Husky(Dog):
    pass

a = Animal()
d = Dog()
h = Husky()
print('isinstance(h, Husky) =', isinstance(h, Husky))
print('isinstance(h, Dog) =', isinstance(h, Dog))
print('isinstance(h, Animal) =', isinstance(h, Animal))
print('isinstance(d, Dog) and isinstance(d, Animal) =', isinstance(d, Dog) and isinstance(d, Animal))
print('isinstance(d, Husky) =', isinstance(d, Husky))

print('isinstance(\'a\', str) =', isinstance('a', str))
print('isinstance(123, int) =', isinstance(123, int))
print('isinstance(b\'a\', bytes) =', isinstance(b'a', bytes))

print('isinstance([1, 2, 3], (list, tuple)) =', isinstance([1, 2, 3], (list, tuple)))
print('isinstance((1, 2, 3), (list, tuple)) =', isinstance((1, 2, 3), (list, tuple)))

print('dir(\'ABC\') =', dir('ABC'))

print('len(\'ABC\') =', len('ABC'))
print('\'ABC\'.__len__() =', 'ABC'.__len__())

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
print('hasattr(obj, \'x\') =', hasattr(obj, 'x'))
print('obj.x =', obj.x)
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))
print('getattr(obj, \'y\') =', getattr(obj, 'y'))
print('obj.y =', obj.y)
print('getattr(obj, \'z\', 404) =', getattr(obj, 'z', 404))

print('hasattr(obj, \'power\') =', hasattr(obj, 'power'))
print('getattr(obj, \'power\') =', getattr(obj, 'power'))
fn = getattr(obj, 'power')
print('fn =', fn)
print('fn() =', fn())