# Задача 30  Вычислить число pi c заданной точностью d. Число d находится в интервале [1e-1, 1e-10]

from decimal import Decimal

d = int(input('Введите точьность вычесления знаков после запятой '))
pi = 3.1415926535

number = Decimal(12)
result = Decimal(3)

for p in range(1, 9):
    result = (result + number / result) / Decimal(2)
    difference = result ** 2 - number

sqrt12 = result
sum = Decimal(1)
sign = -1
long = (2, 3, 5, 6, 8, 9, 12, 14, 15, 18, 20)

for p in range(1, long[d]):
    sum += Decimal(sign) / Decimal((2 * p + 1) * (3 ** p))
    sign = -sign

result = str(sqrt12 * sum)
result = float(result[:12])

print('vallis(1e-',d,') -> (',result, ',', p, ',', '%.10f' % float(pi - result),')')
