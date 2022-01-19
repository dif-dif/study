def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 5, 9, 11, 12, 30, 50]

print(binary_search(my_list, 9))
print(binary_search(my_list, -1))