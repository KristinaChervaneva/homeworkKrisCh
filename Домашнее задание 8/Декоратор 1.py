def decorator1(func):
    def wrapper(*args):
        A = []
        for i in args:
            A.append(i)
        for i in range((len(A))//2):
            A[i], A[len(A) - i - 1] = A[len(A) - i - 1], A[i]
        return func(*A)
    return wrapper

@decorator1
def foo(*args):
    return args


print(foo(10,7,3,5,10,2,1))