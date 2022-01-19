from re import X


x = 55
print('Глобальный х равен', x)

def func_outer():
    x = 2
    print('Локальный x равен', x)

    def func_inner():
        nonlocal x
        x = 42
    
    func_inner()
    print('Локальный х сменился на', x)

func_outer()
print('Глобально х равен', x)
