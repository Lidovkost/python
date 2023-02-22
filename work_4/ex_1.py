import math
a = float(input('введите число '))
b = 0.001
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"
after_point = len(str(b)) - 2
print(round(a, after_point))          # первый способ
a = toFixed(a, after_point)           # второй способ
print(a)