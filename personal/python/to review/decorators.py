"""
Decorators
"""

"""
Single argument decorator
"""


def my_decorator(func):
    def wrap_func(arg):
        print('-------------------------')
        func(arg)
        print('-------------------------')

    return wrap_func


@my_decorator
def hello(greeting):
    print(greeting)


hello('test')

"""
Multiple arguments decorator
"""


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('-------------------------')
        func(*args, **kwargs)
        print('-------------------------')

    return wrap_func


@my_decorator
def hello(greeting, info, emoji=':)'):
    print(greeting, emoji, info)


hello('test', 'ggg')

"""
Performance decorator
"""
from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'took {t2 - t1}secs')
        return result

    return wrapper


"""
Decorator that only allows the function to run if user has 'valid' set to True
"""
user1 = {
    'name': 'Sorna',
    'valid': True  # changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if not args[0]['valid']:
            return print('Not authenticated')
        else:
            print('Authenticated')
            result = fn(*args, **kwargs)
            return result

    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)