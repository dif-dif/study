def printMin(a,b):
    if a < b:
        print(a,'минимально')
    elif a == b:
        print(a, 'равно', b)
    else:
        print(b, 'минимально')

printMin(3,4)
printMin(5,5)

x = 5
y = 4
printMin(x, y)