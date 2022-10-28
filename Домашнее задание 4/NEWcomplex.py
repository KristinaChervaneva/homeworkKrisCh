import math
import numbers

class ComplexNumber:

    def __init__(self, my_a = 0, my_b = 0): #инициализатор
        self.set(my_a, my_b)

    def set(self, my_a, my_b): #сеттер
        self.a = my_a
        self.b = my_b
        return

    def get(self): #геттер
        return self.a, self.b

    def __add__(self, drugoe):
        if isinstance(drugoe, numbers.Number):
            return self.a + drugoe, self.b
        else:
            return self.a + drugoe.a, self.b + drugoe.b

    def __radd__(self, drugoe):
        if isinstance(drugoe, numbers.Number):
            return self.a + drugoe, self.b
        return self.a + drugoe.a, self.b + drugoe.b

    def __sub__(self, drugoe):
        if isinstance(drugoe, numbers.Number):
            return self.a - drugoe, self.b
        else:
            return self.a - drugoe.a, self.b - drugoe.b

    def __rsub__(self, drugoe):
        if isinstance(drugoe, numbers.Number):
            return drugoe - self.a, self.b
        else:
            return drugoe.a - self.a, drugoe.b - self.b

    def __mul__(self, drugoe):
        if isinstance(drugoe, numbers.Number):
            return self.a * drugoe, self.b * drugoe
        else:
            return self.a * drugoe.a - self.b * drugoe.b, self.a * drugoe.b + self.b * drugoe.a

    def __rmul__(self, drugoe):
        if isinstance(drugoe, numbers.Number):
            return self.a * drugoe, self.b * drugoe
        else:
            return drugoe.a * self.a - drugoe.b * self.b, drugoe.a * self.b + drugoe.b * self.a








z1 = ComplexNumber(1, 1)
z2 = ComplexNumber(2, 2)
print(z1 + z2)