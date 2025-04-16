# Question 1
# mov1=input("Enter Movie name")
# mov2=input("Enter Movie name")
# mov3=input("Enter Movie name")
#
# Movie=[]
# Movie.append(mov1)
# Movie.append(mov2)
# Movie.append(mov3)
#
# print(Movie)

# Question2
list1=[1,2,1]
list2=[1,2,3]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
    print("Palindrome")
else:
    print("Not Palindrome ")