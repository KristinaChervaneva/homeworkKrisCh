import math
import numbers

class ComplexNumber:

    def __init__(self, x=0, y=0):
        self.set(x, y)

    def set(self, x, y):
        if isinstance(x, numbers.Number) and isinstance(y, numbers.Number):
            self.a = x
            self.b = y
        else:
            raise ValueError

    def get(self, exp=False):
        if exp == True:
            return self.r, self.phi
        else:
            return self.a, self.b

    def AlgebraToExp(self): #из алгебраической в экспоненциальную
        if self.a == 0:
            raise Exception("Нельзя перевести в экспоненциальную форму, введи другое число (нормальное)")
        self.r = (self.a ** 2 + self.b ** 2) ** 0.5
        if self.a < 0 and self.b > 0:
            self.phi = math.pi - math.atan(abs(self.b) / abs(self.a))
        elif self.a < 0 and self.b < 0:
            self.phi = math.pi + math.atan(abs(self.b) / abs(self.a))
        elif self.a > 0 and self.b < 0:
            self.phi = - math.atan(self.b / self.a)
        else:
            self.phi = math.atan(self.b / self.a)

        return self.r, self.phi

    def ExpToAlgebra(self): #из экспоненциальной в алгебраическую
        self.r = self.a
        self.phi = self.b
        self.x = self.r * math.cos(self.phi)
        self.y = self.x * math.tan(self.phi)

        return self.x, self.y

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
        else:
            raise ValueError

    def __pow__(self, power, modulo=None):

        if self.a == 0 and self.b == 0:
            if power == 0:
                raise Exception('Ноль в нуле не определен')
            else:
                return 0, 0
        else:
            self.r, self.phi = self.convert_v_exp()
            self.r = self.r ** power
            self.phi = self.phi * power
            self.a, self.b = self.r, self.phi
            return self.convert_v_alg()

print("Введи два комплексных числа: в формате a b c d, где a и b Re и Im первого числа, а c и d - Re и Im второго.")
try:
    arr = [float(t) for t in input().split()]
except ValueError:
    print("Надо ввести числа!")
else:
    try:
        A = ComplexNumber(arr[0], arr[1])
        B = ComplexNumber(arr[2], arr[3])
    except IndexError:
        print("Введено меньше 4х чисел")

print("Введи операции: +, -, /, *, == (равенство двух чисел), AlgebraToExp  (перевод в показательную форму каждого), pow  (возведение в степень каждого), abs (взятие модуля от каждого числа)")
oper = input()
try:
    if oper not in ("+", "-", '/', '*', '==', 'conv_exp', 'pow', 'abs'):
        raise TypeError
except TypeError:
    print('Нужно ввести операцию из списка...')


if oper == '+':
    print(A + B)
if oper == '-':
    print(A - B)
if oper == '*':
    print(A * B)
if oper == '/':
    try:
        print(A // B)
    except ZeroDivisionError:
        print('Никто на ноль не делит, введи другое комплексное число')
if oper == 'AlgebraToExp':
    try:
        print('Конвертация первого числа:', A.AlgebraToExp())
    except Exception:
        print('Нельзя конвертировать первое число) Введи другое комплексное число')
    try:
        print('Конвертация второго числа:', B.AlgebraToExp())
    except Exception:
        print('Нельзя конвертировать второе число) Введи другое комплексное число')
if oper == '==':
    print(A == B)

if oper == 'abs':
    print('Модуль первого числа:', abs(A))
    print('Модуль второго числа:', abs(B))

if oper == 'pow':
    print('Введи степень')

    try:
        power = float(input())
    except ValueError:
        print("Введи число!")

    try:
        print('А в степени', power, ':', pow(A, power))
    except Exception:
          print('Степень А определить не удалось: измени степень или первое комплексное число')

    try:
        print('B в степени', power, ':', pow(B, power))
    except Exception:
          print('Степень В определить не удалось: измени степень или второе комплексное число')


