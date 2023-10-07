# ValueError
while True:
    try:
        x = int(input("Enter Int: "))
        print(x)
        break
    except ValueError:
        print("Your value isn't Integer. Print Int...")

# ZeroDivisionError, else, ValueError and Finally(works in any scenario)       
while True:
    try: 
        x = 5
        y = int(input("Divide 5 with any Int except 0: "))
        print(x/y)
    except ZeroDivisionError:
        print("You must type any Int except 0. Try again..")
    except ValueError:
        print("Your value isn't Integer. Print Int...")
    else: 
        break
    finally:
        print("0_0")

# KeyError
dict = {'x': 1, 'y': 2}
try:
    value = dict['z']
except KeyError:
    print("Key error. Key for 'value' doesn't exist")

# TypeError
try:
    result = "10" + 5 
except TypeError as e:
    print("You can't add string to integer")