class MyErr:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                num = int(input('Введите число и нажмите Enter - '))
                self.my_list.append(num)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимый символ")
                check = input(f'Хотите продолжить? Y/N ')

                if check == 'Y' or check == 'y':
                    print(a.my_input())
                elif check == 'N' or check == 'n':
                    return 'Конец'
                else:
                    return 'Конец'