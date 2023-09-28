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
if operation == "+":
    print("Answer is:", plus(a, b))
elif operation == "-":
    print("Answer is:", minus(a, b))
elif operation == "*":
    print("Answer is:", multiply(a, b))
elif operation == "/":
    print("Answer is:", divide(a, b))
else: 
    print("You did something wrong, try againg.")
    
        
