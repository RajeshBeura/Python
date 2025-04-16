# when a function calls itself repeatedly.


# prints n to 1 backwords using recursion
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
#
#
# n=int(input("Enter n "))
# show(n)

# print factorial of number using recursion
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)

n=int(input("Enter a number to find factorial :-  "))

print("factorial of ",n,"==",fact(5))