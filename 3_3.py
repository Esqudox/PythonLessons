def my_func(a, b, c):
    if ((a < b) and (a < c)):
        d = c + b
    elif ((b < c) and (b < a)):
        d = a + c
    else: d = a + b
    return(d)

a = int(input('Введите первый аргумент - '))
b = int(input('Введите второй аргумент - '))
c = int(input('Введите третий аргумент - '))
d = my_func(a, b, c)
print(f'Cумма двух наибольших аргументов - {d}')