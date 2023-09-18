def discriminant (a, b, c):
    D = b**2 - 4*a*c
    return D

print("Hello, that's example of your discriminant function: \n 2x^2 - 6x + 4")
a = int(input("What's your \"A\" parameters: "))
b = int(input("What's your \"B\" parameters: "))
c = int(input("What's your \"C\" parameters: "))
print(discriminant(a, b, c))
