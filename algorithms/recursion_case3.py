def recur_fibo(n):
    # base case
    if n <= 1:
        return n
    else:
    # recursive case
        return(recur_fibo(n-1) + recur_fibo(n-2))

num = int(input())
print(recur_fibo(num))