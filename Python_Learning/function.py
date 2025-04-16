# function is a block of statements that perform a specific task

# def calc_sum(a,b):
#     return (a+b)
#
# print(calc_sum(5,6))

# usd to inr convertor
def convertor(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")


n = float(input("Enter USD value to convert in INR"))
print(type(n))
convertor(n)
