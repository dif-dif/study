while True:
    s = input('Введите пароль: ')
    if s == 'выход' or s == 'exit':
        break
    if len(s) < 8:
        print('Пароль слишком короткий')
        continue
    print('Пароль надежен')