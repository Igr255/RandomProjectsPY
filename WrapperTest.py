import math


class TooManyCallsError(ValueError):
    pass


def limit_calls(max_calls: int = 1, error_message_tail: str = 'called too often'):
    def decorator_function(func):
        def wrapper(a, b):
            wrapper.calls += 1
            if wrapper.calls > max_calls:
                specific_error_message = "function" + ' \'' + func.__name__ + "\' - " + error_message_tail
                raise TooManyCallsError(specific_error_message)
            return func(a, b)
        wrapper.calls = 0
        return wrapper
    return decorator_function


@limit_calls(1, 'that is too much')
def pyth(a,b):
    c = math.sqrt(a ** 2 + b ** 2)
    return c

print(pyth(2,3))
pyth(3,4)