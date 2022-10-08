import math

class ComplexNumber:

    def __init__(self, my_a = 0, my_b = 0): #инициализатор
        self.set(my_a, my_b)

    def set(self, my_a, my_b): #сеттер
        self.a = my_a
        self.b = my_b

    def get(self): #геттер
        return self.a, self.b

    def AlgebraToExp(self):
        self.a, self.b = math.sqrt(self.a * self.a + self.b * self.b), math.atan(self.b / self.a)
        return

    def ExpToAlgebra(self):
        self.a, self.b =

