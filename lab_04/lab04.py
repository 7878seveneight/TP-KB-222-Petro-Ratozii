operators = {'+', '-', '*', '/', '^'}

def zpz(tokens):
    stack = []
    operatorStack = []

    def applyOperator():
        a, b = stack.pop(), stack.pop()
        operator = operatorStack.pop()
        if operator == '+':
            stack.append(b + a)
        elif operator == '-':
            stack.append(b - a)
        elif operator == '*':
            stack.append(b * a)
        elif operator == '/':
            stack.append(int(b / a))
        elif operator == '^':
            stack.append(b ** a)

    for token in tokens:
        if token == '(':
            operatorStack.append(token)
        elif token == ')':
            while operatorStack and operatorStack[-1] != '(':
                applyOperator()
            operatorStack.pop()
        elif token in operators:
            while operatorStack and operatorStack[-1] in operators:
                current_operator = operatorStack[-1]
                priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
                if priority.get(token, 0) <= priority.get(current_operator, 0):
                    applyOperator()
                else:
                    break

            operatorStack.append(token)
        else:
            stack.append(int(token))

    while operatorStack:
        applyOperator()

    return stack.pop()

def main():
    tokens = ["16", "/", "(","5","3","-",")", "3", "^"]
    result = zpz(tokens)
    print(result)

if __name__ == "__main__":
    main()