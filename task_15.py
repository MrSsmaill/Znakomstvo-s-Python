#Задача 15 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

num = int(input('Ввиде число '))
num_list = []
j=1
for i in range(1, num+1):
    num_list.append(j)
    j += j*i

print(num_list)