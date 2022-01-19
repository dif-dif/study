def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n*factorial_recursive(n-1)

def print_factorial(n):
    print('Факториал числа {0} --> {1}'.format(n, factorial_recursive(n)))

print_factorial(int(input()))