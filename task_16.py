#Задача 16  Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

num = int(input('Ввиде число '))
num_sum = 0
for i in range(1, num+1):
    num_sum += (1+1/i)**i

print('Сумма = {:.2f}'.format(num_sum))