"""Задача 13. Напишите программу, в которой пользователь будет задавать две строки, а программа
 - определять количество вхождений одной строки в другой.        """


str_scope = '1285564dasd152asdasd12asdasdaswqe1234'
str_find = '12'

find_count = 0
for i in range(len(str_scope)):
    if str_find == str_scope[i:i+len(str_find)]:
        find_count += 1

print(find_count)
