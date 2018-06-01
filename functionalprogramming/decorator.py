import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **knw):
        print('call %s' % func.__name__)
        return func(*args, **knw)
    return wrapper

@log
def now():
    print('2015-05-25')

now()

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **knw):
            print('%s %s():' %(text, func.__name__))
            return func(*args, **knw)
        return wrapper
    return decorator

@log2('execute')
def now2():
    print('2015-05-25')
now2()
print('now.__name__ =', now.__name__)
print('now2.__name__ =', now2.__name__)