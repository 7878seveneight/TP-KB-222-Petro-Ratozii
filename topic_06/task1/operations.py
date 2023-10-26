import datetime
import os

logFile = "log.txt"
dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(dir, "log.txt")

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

def logs(operation, a, b, result):
    currentDate = datetime.datetime.now()
    date = currentDate.strftime("%Y-%m-%d %H:%M:%S")
    log = f"\n\n\t{date} \nInstance: {a} {operation} {b} = {result} \nOperation: {operation}, First num: {a}, Second num: {b}, Result or operation: {result}"
    with open(path, "a") as file:
        file.write(log)

def logsForExit():
    currentDate = datetime.datetime.now()
    date = currentDate.strftime("%Y-%m-%d %H:%M:%S")
    with open(path, "a") as file:
        file.write(f"\n\n\t{date}\nQuit from program.")

operations = ['Quit', 'quit', '+', '-', '*', '/']