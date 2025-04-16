# Debugging Function Calls
# Create a decorator to print the fuction name and the values of its arguments every time the function is called

def debug(func):
    def wrapper():
        return wrapper()






def greet(name,greeting="Hello"):
    print(f"{greeting}, {name}")

greet("chai",greeting="Hanji ")