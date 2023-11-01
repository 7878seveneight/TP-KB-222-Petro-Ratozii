class CalcFunctions:
    def getFloatValue(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Value is not integer or float. Try againg...")
    def plus (self, a, b):
        return a + b
    def minus (self, a, b):
        return a - b
    def multiply (self, a, b):
        return a * b
    def divide (self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("You can't divide a number by zero. Try againg...")

