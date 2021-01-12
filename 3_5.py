def my_func():
    sum_res = 0
    i = False
    while i == False:
        number = input('Введите числа через пробел, Нажмите Q для выхода - ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                i = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Текущая сумма - {sum_res}')
    print(f'Программа окончена, конечная сумма -  {sum_res}')

my_func()