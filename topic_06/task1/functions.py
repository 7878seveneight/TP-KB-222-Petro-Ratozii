def plus (a, b):
    return a + b
def minus (a, b):
    return a - b
def multiply (a, b):
    return a * b
def divide (a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("You can't divide a number by zero. Try againg...")