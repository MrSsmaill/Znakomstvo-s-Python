#Задача 4 Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
num = float(input('Ввидите число '))
number_dec = str(num-int(num))[2:3]
num_dec = int(number_dec)
if num_dec == 0:
    print('нет')
else:
    print(num_dec)

n = input()
ch = n.find('.')
print (n[ch+1])

num = "6,78"
lst = num.split(",")
print(lst[1][0])

num[num.find(",")+1]

num[num.find(",")]