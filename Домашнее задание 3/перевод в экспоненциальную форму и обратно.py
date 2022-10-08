import math

class ComplexNumber:

    def __init__(self, my_a = 0, my_b = 0): #инициализатор
        self.set(my_a, my_b)
        return

    def set(self, my_a, my_b): #сеттер
        self.a = my_a
        self.b = my_b
        return

    def get(self): #геттер
        return self.a, self.b

    def AlgebraToExp(self):
        self.a, self.b = math.sqrt(self.a * self.a + self.b * self.b), math.atan(self.b / self.a)
        return

    def ExpToAlgebra(self):
        self.a, self.b = self.a * math.cos(self.b), self.a * math.sin(self.b)
        return

z = ComplexNumber(1, 1)
z.AlgebraToExp()
print(*z.get())
z.ExpToAlgebra()
print(*z.get())

