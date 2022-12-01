import time


def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        t = time.time() - start_time
        return res, t
    return wrapper


@decorator
def dinamicaFibon(n):
    if n < 1:
        return
    A = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        A[i] = A[i-1] + A[i-2]
    return A[n-1]

def recursiyaFibon(n):
    if n < 1:
        return
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return recursiyaFibon(n-1) + recursiyaFibon(n-2)


@decorator
def fibon_recursiya(n):
    return recursiyaFibon(n)


res1, t1 = fibon_recursiya(30)
res2, t2 = dinamicaFibon(30)
print('Рекурсия считает за время ', t1, ' сек, а цикл - за ', t2, 'сек')