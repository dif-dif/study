class ShortInputException(Exception):
    '''Пользовательский класс исключения.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter smth --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)

except EOFError:
    print('Why are you gay?')
except ShortInputException as ex:
    print('ShortInputException: Length of the entering string -- {0}; \
        ожидалось, как минимум, {1}'.format(ex.length, ex.atleast))
else:
    print('There is no exception.')