from itertools import cycle

my_list = ['ABC', 14, 12]
stop_count = int(input('Введите количество повторений - '))
count = 0

for el in cycle(my_list):
    print(el)
    if count > stop_count:
        break
    count += 1