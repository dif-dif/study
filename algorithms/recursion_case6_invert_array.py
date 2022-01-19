'''
This programm is reversing an array with recursion.
'''

def reverse(array):
    if len(array) == 0:
        return
    elif len(array) == 1:
        return array
    return [array[len(array) - 1]] + reverse(array[:len(array) - 1])

array = [1, 2, 3, 4]
print(reverse(array))