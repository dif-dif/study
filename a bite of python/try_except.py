try:
    text = input('Write something --> ')
except EOFError:
    print('Why are you gay?')
except KeyboardInterrupt:
    print(' You canceled this operation. Lox.')
else:
    print('You have entered {0}'.format(text))