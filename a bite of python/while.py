number = 42
running = True

while running:
    guess = int(input('Введите целое число: '))

    if guess == number:
        print('Вы угадали')
        running = False

    elif guess < number:
        print('Загаданное число больше этого')

    else:
        print('Загаданное число меньше этого')
else:
    print('Программа остановлена')
    
print('Канец')