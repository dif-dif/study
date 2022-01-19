'''
Сортировка выбором: O(n*2)
'''

def findSmallest(arr):
    smallest = arr[0] # create unsorted array
    smallest_index = 0 # setting the initial index
    '''
    We go through all the elements of the array and find the
    smallest one. Putting it in an array.
    '''
    for i in range(1, len(arr)): 
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = [] # create sorted array
    '''
    Applying function "findSmallest" to our array. Sorted items are
    dying and go to python hell.
    '''
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))