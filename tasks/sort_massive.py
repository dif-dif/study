myList = [9, 1, 5, 9, 4, 2, 7, 2, 9, 5, 3]
occurrences = []
 
for item in myList :
    count = 0
    for x in myList :
        if x == item :
            count += 1
    occurrences.append(count)

duplicates = set()
index = 0
while index < len(myList) :
    if occurrences[index] != 1 :
        duplicates.add(myList[index])
    index += 1

print(duplicates)