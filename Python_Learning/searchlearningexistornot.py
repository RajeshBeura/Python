from traceback import print_tb

with open("learning.txt","r") as f:
    data = f.read()
    if(data.find("learning")!=-1):
        print("Found")
    else:
        print("Not Found")
