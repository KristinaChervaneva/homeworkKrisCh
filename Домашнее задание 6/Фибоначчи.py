def fibonacci(n):
    x1, x2 = 0, 1
    for __ in range(n):
        yield x1
        x1, x2 = x2, x1 + x2


N = int(input()) #Вводим номер числа фибоначчи
for i in fibonacci(N):
    print(i, end=' ')