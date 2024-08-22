import math
def square(a):
    b = a * a
    return math.ceil(b)

a = float(input("Введите сторону квадрата: "))
print(square (a))