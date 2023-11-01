import datetime
import os

class CalcOperatoins:
    def __init__(self):
        self.operations = ['+', '-', '*', '/', 'Quit', 'quit']
    def getOperation(self, operations):
        while True:
            operation = input("If you want to quit the program - type \"Quit\" \nWhat's your operation (+, -, *, /): ")
            if operation in operations:
                return operation
            else:
                print("You did something wrong, write your operation (+, -, *, /)")
    def logs(self, operation, a, b, result):
        dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(dir, "log.txt")
        currentDate = datetime.datetime.now()
        date = currentDate.strftime("%Y-%m-%d %H:%M:%S")
        log = f"\n\n\t{date} \nInstance: {a} {operation} {b} = {result} \nOperation: {operation}, First num: {a}, Second num: {b}, Result or operation: {result}"
        with open(path, "a") as file:
            file.write(log)
    def logsForExit(self):
        dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(dir, "log.txt")
        currentDate = datetime.datetime.now()
        date = currentDate.strftime("%Y-%m-%d %H:%M:%S")
        with open(path, "a") as file:
            file.write(f"\n\n\t{date}\nQuit from program.")

