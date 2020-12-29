start = int(input('Начнем с - '))
goal = int(input('Наша цель - '))
if start >= goal:
    print('Вы ставите перед собой неправильные цели')
else:
    print('\nРезультат:\n')
    distance = start
    count_day = 1
    print(f'{count_day}-й день: {round(distance, 2)} км')
    while True:
        count_day += 1
        distance = distance * 1.1
        print(f'{count_day}-й день: {round(distance, 2)} км')
        if distance < goal:
            continue
        elif distance >= goal:
            print(f'\nНа {count_day}-й день спортсмен достиг результата - не менее {goal} км')
        break
