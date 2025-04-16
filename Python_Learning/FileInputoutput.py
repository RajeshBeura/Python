#python can be used to perform operations on a file(read & write data)
#Types of all files 1-Text file-.txt,.docx,.log etc 2.Binary Files :- .mp4,.mov,.png,.jpeg etc
from sys import modules

# f=open("doc.txt","r")
# data=f.read()
# print(data)
# print(type(data))
# f.close()
#
# with open("doc.txt","r") as f:
#     data=f.read()
# print(data)



# Deleting a file
# using the os module
# Module(like a code library)is a file written by annother programmer that generally has a functions we can use.

# import os
# os.remove("doc.txt")

# with open("practice.txt","w") as f:
#     f.write("Hi everyone \nwe are learning file I/O \n")
#     f.write("using Java, I like programming in java \n")
#
# with open("practice.txt","r") as f:
#     data=f.read()
# newdata=data.replace("Java","python")
# print(newdata)


# def check_for_word():
#     word="learning"
#     with open("practice.txt","r") as f:
#         data=f.read()
#         if(data.find(word)!= -1):
#             print("Found")
#         else:
#             print("not Found")

def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1

    return -1

check_for_line()