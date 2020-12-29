n = int(input('Введите любую цифру - '))

# переводим n str, для составления числа, после чего переводим обратно в int и складываем
summa = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))

print(f'Сумма n + nn + nnn = {summa}')
