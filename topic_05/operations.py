def getFloatValue(promt: str):
    while True:
        try:
            return float(input(promt))
        except ValueError:
            print("Value is not integer or float. Try againg...")

def getOperation(operations):
    while True:
        operation = input("If you want to quit the program - type \"Quit\" \nWhat's your operation (+, -, *, /): ")
        if operation in operations:
            return operation
        else:
            print("You did something wrong, write your operation (+, -, *, /)")

operations = ['Quit', 'quit', '+', '-', '*', '/']