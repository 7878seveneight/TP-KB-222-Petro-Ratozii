def plus (a, b):
    return a + b
def minus (a, b):
    return a - b
def multiply (a, b):
    return a * b
def divide (a, b):
    return a / b

while True:
    operation = input("If you want to quit the program - type \"Quit\" \nWhat's your operation (+, -, *, /): ")
    if operation == "Quit" or operation == "quit":
        print("Quiting the program...")
        break
    elif operation == "+" or operation == "-" or operation == "*" or  operation == "*" or operation == "/": 
        a = int(input("Your first num: "))
        b = int(input("Your second num: "))

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