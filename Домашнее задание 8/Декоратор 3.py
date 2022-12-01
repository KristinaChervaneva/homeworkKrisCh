def decorator3(func):
    def wrapper(x, y):
        try:
            func(x, y)
        except BaseException:
            return 'error'
        return func(x, y)
    return wrapper


@decorator3
def foo(a, b):
    return a/b


print(foo(5, 4))
print(foo(16, 2))