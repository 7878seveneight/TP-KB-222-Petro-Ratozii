from functions import *
from operations import *

while True:
    operation = getOperation(operations)
    if operation == "Quit" or operation == "quit":
        print("Quiting the program...")
        break
    else:
        a = getFloatValue("Your first num: ")
        b = getFloatValue("Your second num: ")

        match(operation):
            case "+": 
                print("Answer is:", plus(a, b))
            case "-": 
                print("Answer is:", minus(a, b))
            case "*":
                print("Answer is:", multiply(a, b))
            case "/":
                print("Answer is:", divide(a, b))