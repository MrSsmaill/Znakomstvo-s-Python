# Задача 14 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = input('Ввиде число ')
summa = 0
for i in range(len(num)):
   summa += int(num[i])
print(summa)
