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

    def __floordiv__(self, drugoe):
        if isinstance(drugoe, numbers.Number):
            return round(self.a / drugoe, 3), round(self.b / drugoe, 3) #возвращаем округленное значение с 3мя знаками после запятой
        else:
            return (self.a * drugoe.a + self.b * drugoe.b) / (drugoe.a ** 2 + drugoe.b ** 2), (
                        self.b * drugoe.a - self.a * drugoe.b) / (drugoe.a ** 2 + drugoe.b ** 2)

    def __rfloordiv__(self, drugoe):
        if isinstance(drugoe, numbers.Number):
            return round(drugoe / self.a, 3), round(drugoe / self.b, 3)
        return (drugoe.a * self.a + drugoe.b * self.b) / (self.a ** 2 + self.b ** 2), (
                    drugoe.b * self.a - drugoe.a * self.b) / (self.a ** 2 + self.b ** 2)








z1 = ComplexNumber(1, 1)
z2 = ComplexNumber(2, 2)
print(z1 + z2)
print(z1 // z2)
print(z1 // 7)