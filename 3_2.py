def my_func(a, b, c, d, e):
    inform = {'Имя': a, 'Фамилия': b, 'Возраст': c, 'Город': d, 'Телефон': e}
    return(inform)

a = str(input('Введите имя - '))
b = str(input('Введите фамилию - '))
c = str(input('Введите возраст - '))
d = str(input('Введите город - '))
e = str(input('Введите номер телефона - '))

inform = my_func(a, b, c, d, e)
print(inform)