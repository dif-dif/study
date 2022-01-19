def sumTill(targetNumber):
    # base case
    if targetNumber == 1:
        return targetNumber
    # recursive case
    else:
        return targetNumber + sumTill(targetNumber - 1)

targetNumber = int(input())
print(sumTill(targetNumber))