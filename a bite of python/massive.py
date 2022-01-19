# A = [1, 2, 3, 4, 5]

# for x in A:
#     x = x * x
#     print(x)


# A = [0] * 1000
# top = 0
# x = int(input())
# while x != 0:
#     A[top] = x
#     top += 1
#     x = int(input())
# for k in range (4, -1, -1):
#     print(A[k])


A = [1, 2, 3, 4, 5, 7, 12, 9, 6]
# B = []                     можно сделать в одну
# for x in A:                строчку
#     if x % 2 == 0:
#         B.append (x**2)
B = [0 if x < 0 else x**2 for x in A if x % 2 == 0]
print(B)