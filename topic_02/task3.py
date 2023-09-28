def plus (a, b):
    return a + b
def minus (a, b):
    return a - b
def multiply (a, b):
    return a * b
def divide (a, b):
    return a / b

a = int(input("Your first num: "))
b = int(input("Your second num: "))
operation = input("What's your operation (+, -, *, /): ")

match(operation):
    case "+": 
        print("Answer is:", plus(a, b))
    case "-": 
        print("Answer is:", minus(a, b))
    case "*":
        print("Answer is:", multiply(a, b))
    case "/":
        print("Answer is:", divide(a, b))
    case _:
        print("You did something wrong, try againg.")