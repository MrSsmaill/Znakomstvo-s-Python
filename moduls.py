import random


def random_num_list(size, min_value, max_value):
    num_random = []
    for i in range(size):
        num_random.append(int(random.randint(min_value, max_value)))
    return num_random


def coefficient(k):
    coeff = random_num_list(k+1, 0, 100)
    while coeff[k] == 0:
        coeff.insert(k,int(random.randint(0, 100)))
    return coeff

def polynomial(coeff):

    list_polyn = []
    for i in range(len(coeff)):
        if i >= 2 and coeff[i] != 0:
            list_polyn.append(str(coeff[i]) + 'x^' + str(i))
        elif i == 1 and coeff[i] != 0:
            list_polyn.append(str(coeff[i]) + 'x')
        elif i == 0 and coeff[i] != 0:
            list_polyn.append(str(coeff[i]))
    list_polyn.reverse()
    str_polyn='+'.join(list_polyn)
    str_polyn+='=0'
    return str_polyn
