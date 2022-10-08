class ComplexNumber:

    def __init__(self, my_a = 0, my_b = 0): #инициализатор
        self.set(my_a, my_b)

    def set(self, my_a, my_b): #сеттер
        self.a = my_a
        self.b = my_b

    def get(self): #геттер
        return self.a, self.b

