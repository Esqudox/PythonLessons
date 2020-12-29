a_str = input('Введите строку - ')
a_list = []
i = 1
for el in range(a_str.count(' ') + 1):
    a_list = a_str.split()
    if len(str(a_list)) <= 10:
        print(f'{i} {a_list [el]}')
        i += 1
    else:
        print(f'{i} {a_list [el][0:10]}')
        i += 1
