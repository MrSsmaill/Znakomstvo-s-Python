# Задача 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
from time import time

num = int(input('Введите число '))
num_list = []


def fibonachi(n):
    if n in (1, 2):
        return 1
    return fibonachi(n - 1) + fibonachi(n - 2)

fibonachi_line = []
for i in range(1, num + 1):
    fibonachi_line.append(fibonachi(i))
revers_fibonachi_line = fibonachi_line.copy()
revers_fibonachi_line.reverse()
i = -2
while i >= -len(revers_fibonachi_line):
    revers_fibonachi_line[i] *= -1
    i -= 2
revers_fibonachi_line.append(0)
for item in fibonachi_line:
    revers_fibonachi_line.append(item)
print(revers_fibonachi_line)
