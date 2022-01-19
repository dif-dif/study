x = 42

def func():
    global x
    print('x равен', x)
    x = 2
    print('х заменился на', x)

func()
print('x равен', x)
