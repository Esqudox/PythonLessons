class Machines:

    def __init__(self, name, price, quantity):

        self.name = name
        self.price = price
        self.quantity = quantity
        self.storage = []
        self.storage_print = []
        self.units = {'Название модели': self.name, 'Цена': self.price, 'Количество': self.quantity}


    def __str__(self):
        return f'{self.name}: стоимость - {self.price}, количество - {self.quantity}'



    def supply(self):

        while True:
            try:
                unit_name = input('-------------------------\nВведите название - ')
                unit_price = int(input('Введите цену - '))
                unit_q = int(input('Введите количество - '))
                unique = {'Название модели': unit_name, 'Цена': unit_price, 'Количество': unit_q}
                self.units.update(unique)
                self.storage.append(self.units)
                print(f'Текущий список - {self.storage}')

            except:
                return 'Ошибка ввода'


            print('Для выхода нажмите <Q>, Чтобы продолжить, нажмите <Enter>')
            check = input()
            if check == 'q' or 'Q':
                self.storage_print.append(self.storage)
                print(f'Склад - {self.storage_print}')
            else:
                return Machines.supply(self)

class Xerox(Machines):

    def __init__(self, name, price, quantity, speed):
        super().__init__(name, price, quantity)
        self.speed = speed

    def __str__(self):
        return f'{self.name}: стоимость - {self.price}, количество - {self.quantity}, скорость работы - {self.speed} листов в час'

    @property
    def to_copy(self):
        return f'\n{self.name} is copying...'

class Printer(Machines):

    def __init__(self, name, price, quantity, type):
        super().__init__(name, price, quantity)
        self.type = type

    def __str__(self):
        return f'{self.name}: стоимость - {self.price}, количество - {self.quantity}, тип работы - {self.type}'


    @property
    def to_print(self):
        return f'\n{self.name} is printing...'


class Scanner(Machines):

    def __init__(self, name, price, quantity, connection):
        super().__init__(name, price, quantity)
        self.connection = connection

    def __str__(self):
        return f'{self.name}: стоимость - {self.price}, количество - {self.quantity}, связь по {self.connection}'

    @property
    def to_scan(self):
        return f'\n{self.name} is scanning...'

unit_1 = Printer('Samsung', 24000, 3, 'laser')
unit_2 = Xerox('Xerox', 45000, 2, 60)
unit_3 = Scanner('HP', 13000, 5, 'wi-fi')
print(unit_1)
print(unit_2)
print(unit_3)
print(unit_1.to_print)
print(unit_2.to_copy)
print(unit_3.to_scan)

print(unit_1.supply())
print(unit_2.supply())
print(unit_3.supply())
