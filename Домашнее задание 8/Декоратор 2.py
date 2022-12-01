def decorator2(func):
    def wrapper(*args):
        A = func(*args)
        print(args)
        return A
    return wrapper

@decorator2
def foo(*args):
    a = 0
    for i in args:
        a += i
    return a


print(foo(10, 7, 3, 5, 10, 2, 1))
