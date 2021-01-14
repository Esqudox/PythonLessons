numbers = [12, 15, 3, 14, 124, 34, 12, 56, 2, 17]

new = [el for num, el in enumerate(numbers) if numbers[num - 1] < numbers[num]]

print(f'Текущий список - {new}')