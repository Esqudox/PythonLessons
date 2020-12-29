
goods = []
features = {'Название': '', 'Цена': '', 'Количество': '', 'Ед': ''}
analytics = {'Название': [], 'Цена': [], 'Количество': [], 'Ед': []}
num = 0
feature_ = None
menu = None
while True:
    menu = input('Ввод - Enter, Выход - q, Аналитика - a')
    if menu == 'q':
        break
    num += 1
    if menu == 'a':
        print(f'\nИнформация о товаре\n')
        for key, value in analytics.items():
            print(f'\n{key[:25]}: {value}')
    for f in features.keys():
        feature_ = input(f'Введите "{f}" - ')
        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
...
goods = int(input("Введите количество товара "))
n = 1
my_dict = []
my_list = []
my_analys = {}
while n <= goods:
    my_dict = dict({'Название': input("Введите название "), 'Цена': input("Введите цену "),
                    'Количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
    my_list.append((n, my_dict))
    n += 1
    my_analys = dict(
        {'Название': my_dict.get('Название'), 'Цена': my_dict.get('Цена'), 'Количество': my_dict.get('Количество'),
         'ед': my_dict.get('ед')})
print(my_list)
print(my_analys)