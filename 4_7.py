from itertools import count
from math import factorial

def my_gen():
    for el in count(1):
        yield factorial(el)

g = my_gen()
x = 0
n = int(input('Введите n - '))
for i in g:
    if x < n:
        print(i)
        x += 1
    else:
        break