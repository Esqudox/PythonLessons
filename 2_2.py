n = int(input("Количество элементов - "))
a_list = []
i = 0
el = 0
while i < n:
    a_list.append(input("Введите элемент - "))
    i += 1

for elem in range(int(len(a_list)/2)):
        a_list[el], a_list[el + 1] = a_list[el + 1], a_list[el]
        el += 2
print(a_list)
