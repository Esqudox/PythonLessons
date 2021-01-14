from functools import reduce

def res(a, b):
    return a * b

print(f'Четные числа от 100 до 1000 - {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Произведение четных чисел от 100 до 1000 - {reduce(res, [el for el in range(99, 1001) if el % 2 == 0])}')