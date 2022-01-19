def printPattern(targetNumber):
    # base case

    if (targetNumber <= 0):
        print(targetNumber)
        return

    # recirsive case

    print(targetNumber)
    printPattern(targetNumber - int((n / 2)))
    print(targetNumber)

#driver program

n = int(input())
printPattern(n)