from itertools import count

start_number = int(input('Введите стартовое число - '))
stop_number = int(input('Введите конечное число - '))
for el in count(start_number):
    print(el)
    if el >= stop_number:
        break
        