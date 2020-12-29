
season_list = ['Winter', 'Spring', 'Summer', 'Autumn']
season_dict = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Autumn'}

while True:
    my_month = int(input('Month number - '))

    if my_month == 1 or my_month == 2 or my_month == 12:
        print(f'Your season is {season_list[0]}')
        print(f'Your season is {season_dict.get(1)}')
        break
    elif my_month == 3 or my_month == 4 or my_month == 5:
        print(f'Your season is {season_list[1]}')
        print(f'Your season is {season_dict.get(2)}')
        break
    elif my_month == 6 or my_month == 7 or my_month == 8:
        print(f'Your season is {season_list[2]}')
        print(f'Your season is {season_dict.get(3)}')
        break
    elif my_month == 9 or my_month == 10 or my_month == 11:
        print(f'Your season is {season_list[3]}')
        print(f'Your season is {season_dict.get(4)}')
        break
    else:
        print('Wrong month, try again')
        continue
        