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

    def AlgebraToExp(self): #из алгебраической в экспоненциальную
        self.a, self.b = math.sqrt(self.a * self.a + self.b * self.b), math.atan(self.b / self.a)
        return

    def ExpToAlgebra(self): #из экспоненциальной в алгебраическую
        self.a, self.b = self.a * math.cos(self.b), self.a * math.sin(self.b)
        return

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

    def __str__(self):
        if self.b > 0:
            return str(self.a) + ' + i*' + str(self.a)
        if self.b < 0:
            return str(self.a) + ' - i*' + str(-1 * self.b)
        return str(self.a)

    def __eq__(self, drugoe):
        if isinstance(drugoe, numbers.Number):
            return (self.a == drugoe and self.b == 0)
        else:
            return self.a == drugoe.a and self.b == drugoe.b

    def __abs__(self):
        return (self.a ** 2 + self.b ** 2) ** 0.5

    def __getitem__(self, key): #вызов действительной и мнимой части через 0 и 1
        if key == 0:
            return self.a
        elif key == 1:
            return self.b

    def __setitem__(self, key, value):
        if key == 0:
            self.a = value
        elif key == 1:
            self.b = value


z1 = ComplexNumber(1, 1)
z2 = ComplexNumber(2, 2)
print(z1 + z2)
print(z1 // z2)
print(z1 // 7)
print(z2[1])