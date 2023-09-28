import math

def discriminant (a, b, c):
    D = b**2 - 4*a*c
    return D

def rootsFunc (a, b, c):
    disc = discriminant(a, b, c)
    if disc < 0:
        print("Can't find roots, your discriminant is lower or equals zero. Your equation has no roots. Try againg.")
    elif disc == 0:
        x1 = -b / (2 * a)
        return x1
    else:
        x1 = (-b + math.sqrt(disc)) / (2 * a)
        x2 = (-b - math.sqrt(disc)) / (2 * a)
        return x1, x2

print("Hello, that's example of your discriminant function: \n 2x^2 - 6x + 4")
a = int(input("\tWhat's your \"A\" parameters: "))
b = int(input("\tWhat's your \"B\" parameters: "))
c = int(input("\tWhat's your \"C\" parameters: "))
print(f"Your discriminant is {discriminant(a, b, c)}")

print("Your roots:", rootsFunc(a, b, c))
