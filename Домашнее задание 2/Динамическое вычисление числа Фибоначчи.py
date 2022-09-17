fib1 = fib2 = 1

n = input('Номер элемента ряда Фибоначчи: ')
n = int(n) - 2

while n > 0:
    fib1, fib2 = fib2, fib1 + fib2
    n -= 1

print('Значение этого элемента: ', fib2)
