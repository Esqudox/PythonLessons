def my_func(a, b):
    if (b != 0):
        c = a / b
    else:
        c = print('На ноль делить нельзя')
    return(c)


a = int(input('Введите Частное - '))
b = int(input('Введите делитель - '))
c = my_func(a, b)
print(c)