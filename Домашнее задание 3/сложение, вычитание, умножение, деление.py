import math

class ComplexNumber:

    def __init__(self, my_a = 0, my_b = 0): #инициализатор
        self.set(my_a, my_b)

    def set(self, my_a, my_b): #сеттер
        self.a = my_a
        self.b = my_b
        return

    def get(self): #геттер
        return self.a, self.b

    def AlgebraToExp(self): #из алгебраической в экспоненциальную
        self.a, self.b = math.sqrt(self.a * self.a + self.b * self.b), math.atan(self.b / self.a)
        return

    def ExpToAlgebra(self): #из экспоненциальную в алгебраическую
        self.a, self.b = self.a * math.cos(self.b), self.a * math.sin(self.b)
        return

def summa(self, drugoe):
    return ComplexNumber(self.a + drugoe.a, self.b + drugoe.b)


def raznost(self, drugoe):
    return ComplexNumber(self.a - drugoe.a, self.b - drugoe.b)


def proizvedenie(self, drugoe):
    return ComplexNumber(self.a * drugoe.a - self.b * drugoe.b, self.b * drugoe.a + self.a * drugoe.b)


def chastnoe(self, drugoe):
    return ComplexNumber((self.a * drugoe.a + self.b * drugoe.b) / ((drugoe.a) ** 2 + (drugoe.b) ** 2),
                    (self.b * drugoe.a - drugoe.b * self.a) / ((drugoe.a) ** 2 + (drugoe.b) ** 2))




z1 = ComplexNumber(1, 1)
z2 = ComplexNumber(2, 2)
z = proizvedenie(z1, z2)
print(*z.get())
