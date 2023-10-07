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

def getIntValue(promt: str):
    while True:
        try:
            return int(input(promt))
        except ValueError:
            print("Value is not integer. Try againg...")

while True:
    operation = input("If you want to quit the program - type \"Quit\" \nWhat's your operation (+, -, *, /): ")
    if operation == "Quit" or operation == "quit":
        print("Quiting the program...")
        break
    elif operation == "+" or operation == "-" or operation == "*" or  operation == "*" or operation == "/": 
        a = getIntValue("Your first num: ")
        b = getIntValue("Your second num: ")

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
    else:
        print("You did something wrong, write your operation (+, -, *, /)")