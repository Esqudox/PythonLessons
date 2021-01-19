def summary():
    with open('5_5.txt', 'w+') as f:
        try:
            line = input('Enter numbers - ')
            f.writelines(line)
            num = line.split()

            print(sum(map(int, num)))
        except IOError:
            print('File error')
        except ValueError:
            print('Wrong input')

summary()