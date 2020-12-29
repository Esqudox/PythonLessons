
my_list = [9, 7, 5, 5, 3]
print(f'Рейтинг - {my_list}')
num = int(input('Введите цифру - '))
while True:
    for el in range(len(my_list)):
        if my_list[el] == num:
            my_list.insert(el+1, num)
            break
        elif my_list[0] < num:
            my_list.insert(0, num)
            break
        elif my_list[-1] > num:
            my_list.append(num)
            break
        elif my_list[el] > num and my_list[el + 1] < num:
            my_list.insert(el+1, num)
            break
    print(f'Текущий рейтинг - {my_list}')
    num = int(input('Введите цифру - '))
