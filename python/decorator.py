# https://stackoverflow.com/questions/1263451/python-decorators-in-classes

import functools

class Test:
    def _exception(func):
        @functools.wraps(func)
        def wrapper(self):
            try:
                func(self)
            except Exception as e:
                print(f'{func.__name__}: Error: {e}')
        return wrapper

    @_exception
    def bar(self):
        print "normal call"

test = Test()
test.bar()
