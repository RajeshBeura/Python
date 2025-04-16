# class Student:
#     name="Rajesh"
#
#
# s1=Student()
# print(s1.name)

# class Car:
#     color= "blue"
#     brand="BMW"
#
#
# car1=Car()
# print(car1.color)
# print(car1.brand)

# ///constructor

# class Student:
#     def __init__(self):
#         print("Add new Student")
#     name="Rajesh"
#
#
# s1=Student()
# print(s1.name)

class Student:
    def __init__(self,fullname):
        self.name=fullname
        print("Add new Student")



s1=Student("Rajesh")
print(s1.name)


# Static Method - methods that do not use the self parameter (work at class level)

class Student:
    @staticmethod
    def college():
        print("ABC College")