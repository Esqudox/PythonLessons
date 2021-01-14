numbers = [3, 2, 1, 14, 3, 17, 17, 11, 10, 2, 3]

new = [el for el in numbers if numbers.count(el) == 1]

print(f'Числа, не имеющие повторений - {new}')