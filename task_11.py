#Задача 11. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

num=int(input('Ввидите N '))
num_list=[]
n=1
for i in range(num):
    num_list.append(n)
    n*=-3
print(num_list)