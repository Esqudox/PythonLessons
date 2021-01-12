def my_func(a, b):
    c = 1 / (a ** (-b))
    return(c)

a = int(input('Введите число - '))
b = int(input('Введите отрицательную степень - '))
c = my_func(a, b)
print(c)


def my_func(a, b):
    k = 1
    while (k <= abs(b)):
        c = 1 / a
        a = a * a
        k += 1
        continue
    return(c)

a = int(input('Введите число - '))
b = int(input('Введите отрицательную степень - '))
c = my_func(a, b)
print(c)
