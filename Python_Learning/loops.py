# LOOPS are used to repeat instruction
                    #While
# i=1
# while i<=5:
#     print("hello")
#     i+=1

            # for loop -> for use for sequential traversal. for traversing list,string, tuples etc
# # for loop
# nums=(1,2,3,5)
# for val in nums:
#         print(val)
#
# # for loop with else
# veg=["chilli","mushroom","onion"]
# for el in veg:
#         print(el)
# else:
#     print("END")


# # multiplication table print
# n=int(input("Enter number"))
#
# for i in range(1,11,1):
#     print(n*i)

# # find sum of n natural numbers
# n=int(input("Enter n"))
#
# sum=0
# for i in range(1,n+1,1):
#     sum+=i
#
# print("sum of ", n ,"natural number is",sum)

# find factorial of n natural numbers
n=int(input("Enter n"))

fact=1
for i in range(1,n+1,1):
    fact*=i

print("factorial of ", n ,"natural number is",fact)