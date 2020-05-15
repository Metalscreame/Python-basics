import time

from functools import wraps


def decorator(f):
    @wraps(f) # works without this. with this if you make func.__name__ - it will return actual func name, not wrapper one.
    def wrapper(*args, **kwargs):  # *args, **kwargs - so that it can be used by all funcs with every ammount of args
        start_time = time.time()
        res = f(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print("Took time {}".format(elapsed_time.__str__()))
        return res

    return wrapper


@decorator
def wrapper_func():
    print("doing")


@decorator
def multi_returner(one, two):
    return one, two


wrapper_func()

one, two = multi_returner(1, 2)
print(one, two)
