file_name = input('Введите название файла - ')
f = open(file_name, 'w')
while True:
    s = input()
    if s == '':
        break
    f.write(s+'\n')
f.close()