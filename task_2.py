#Задача 2 Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

num_1=int(input('Введите число 1 = '))
num_2=int(input('Введите число 2 = '))
num_3=int(input('Введите число 3 = '))
num_4=int(input('Введите число 4 = '))
num_5=int(input('Введите число 5 = '))

list_num =(num_1,num_2,num_3,num_4,num_5)
max = list_num[0]

for el in list_num:
    if max<el:
        max=el

print(max)