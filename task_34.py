# Задача 34 (Усложненное). Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import moduls
import random
k = 5 # Задана натуральная максимальня степень

def coefficients_polynomial(polynomial,k):
    coeff_polynom=[]
    for j in range(k+1):
        coeff_polynom.append(0)
    for i in range(len(polynomial)):
        if polynomial[i].find('x')!=-1:
            if polynomial[i][-1:]=='x':
                coeff_polynom[1]=polynomial[i][:-1]
            else:
                coeff_polynom[int(polynomial[i][-1:])]=str(polynomial[i])[:polynomial[i].find('x')]
        else:
            coeff_polynom[0]=polynomial[i]
    return coeff_polynom


my_file = open("polynomial_1.txt", "w+")
my_file.write(moduls.polynomial(moduls.coefficient(int(random.randint(1, k)))))
my_file.close()
my_file = open("polynomial_2.txt", "w+")
my_file.write(moduls.polynomial(moduls.coefficient(int(random.randint(1, k)))))
my_file.close()

my_file = open("polynomial_1.txt", "r")
str_polynomial_1 = my_file.read()
my_file.close()
my_file = open("polynomial_2.txt", "r")
str_polynomial_2 = my_file.read()
my_file.close()

polynomial_1=str_polynomial_1.split('=')
polynomial_2=str_polynomial_2.split('=')

polynomial_1=polynomial_1[0].split('+')
polynomial_2=polynomial_2[0].split('+')

polynomial_1=coefficients_polynomial(polynomial_1,k)
polynomial_2=coefficients_polynomial(polynomial_2,k)

sum_polynomials=[]
for i in range(k+1):
    sum_polynomials.append(int(polynomial_1[i])+int(polynomial_2[i]))

my_file = open("polynomial_3.txt", "w+")
my_file.write(moduls.polynomial(sum_polynomials))
my_file.close()





