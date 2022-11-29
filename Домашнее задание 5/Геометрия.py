class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

def length(a,b):
    return ((a.get_x() - b.get_x()) ** 2 + (a.get_y() - b.get_y()) ** 2)**0.5

class Shape:
    def __init__(self, type = 'Фигура'):
        self._type = type

    def __str__(self):
        return (str(self._type) + "   Площадь:  " + str(self.area()) + "   Периметр:  " +  str(self.perimeter()))

class Triangle(Shape):

    def __init__(self, p1, p2, p3, type = "Треугольник"):
        super().__init__(type)
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3
        self._dist1 = length(self._p1, self._p2)
        self._dist2 = length(self._p2, self._p3)
        self._dist3 = length(self._p1, self._p3)

    def perimeter(self):
        return round(self._dist1 + self._dist2 + self._dist3, 2)

    def area(self):
        a = self.perimeter()/2
        return round((a * (a - self._dist1) * (a - self._dist2) * (a - self._dist3)) ** 0.5, 2)

class Quadrangle(Shape):

    def __init__(self, p1, p2, p3, p4, type = "Четырехугольник"):
        super().__init__(type)
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3
        self._p4 = p4
        self._dist1 = length(self._p1, self._p2)
        self._dist2 = length(self._p2, self._p3)
        self._dist3 = length(self._p3, self._p4)
        self._dist4 = length(self._p1, self._p4)

    def perimeter(self):
        return round(self._dist1 + self._dist2 + self._dist3 + self._dist4, 2)

class Circle(Shape):
    def __init__(self, radius, centre, type = "Круг"):
        super().__init__(type)
        self._radius = radius
        self._centre = centre

    def area(self):
        import math
        return length(self._centre, self._radius) ** 2 * math.pi

    def perimeter(self):
        import math
        return 2 * length(self._centre, self._radius) * math.pi