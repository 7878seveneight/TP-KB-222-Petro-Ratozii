from functions import *
from operations import *

while True:
    oper = CalcOperatoins()
    operation = oper.getOperation(oper.operations)
    if operation == "Quit" or operation == "quit":
        print("Quiting the program...")
        oper.logsForExit()
        break
    else:
        func = CalcFunctions()
        oper = CalcOperatoins()
        a = func.getFloatValue("Your first num: ")
        b = func.getFloatValue("Your second num: ")

        match(operation):
            case "+": 
                print("Answer is:", result := func.plus(a, b))
            case "-": 
                print("Answer is:", result := func.minus(a, b))
            case "*":
                print("Answer is:", result := func.multiply(a, b))
            case "/":
                print("Answer is:", result := func.divide(a, b))
        oper.logs(operation, a, b, result)