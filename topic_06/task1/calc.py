from functions import *
from operations import *

while True:
    operation = getOperation(operations)
    if operation == "Quit" or operation == "quit":
        print("Quiting the program...")
        logsForExit()
        break
    else:
        a = getFloatValue("Your first num: ")
        b = getFloatValue("Your second num: ")

        match(operation):
            case "+": 
                print("Answer is:", result := plus(a, b))
            case "-": 
                print("Answer is:", result := minus(a, b))
            case "*":
                print("Answer is:", result := multiply(a, b))
            case "/":
                print("Answer is:", result := divide(a, b))
        logs(operation, a, b, result)