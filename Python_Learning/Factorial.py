#
#
# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     print(fact)
# factorial(5)
#
from math import factorial


# //recursion
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
#
#
# show(5)


def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

n=int(input("Enter a Number to find factorial"))


print("factorial of ",n,"==",fact(5))
