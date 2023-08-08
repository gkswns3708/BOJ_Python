import functools

def add(x, y):
    return x + y

def outer(x):
    def inner(y):
        return x + y
    return inner

print(functools.partial(add, 10)(10), outer(10)(10))