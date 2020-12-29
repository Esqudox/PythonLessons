a = int(input('Введите время в секундах - '))
if a < 86400:
    hours = a // 3600
    a = a - hours * 3600
    minutes = a // 60
    a = a - minutes * 60
    seconds = a
    print(f'\nВремя в формате чч:мм:сс - {hours}:{minutes}:{seconds}')
else:
    print('\nСлишком много секунд, введите значение меньше 86400')
    