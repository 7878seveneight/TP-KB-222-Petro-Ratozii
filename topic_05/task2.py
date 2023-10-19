import requests
def listAndState():
    list = {elem["cc"]: elem["rate"] for elem in data}
    print(f"Current state of UAH to {currency} is {list[currency]}")
    return list
def getFloatAmount():
    while True:
        try:
            amount = float(input("Amount to calculate: "))
            return amount
        except ValueError:
            print("Use numbers for amount.")

response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json")
data = response.json()

option = ["USD", "EUR", "PLN"]

while True:
    operation = input("If you want to convert UAH to USD, EUR, PLN - type '1'\nIf you want to convert USD, EUR, PLN to UAH - type '2'\n  If you want to quit - type 'Quit'\n\tOption: ")
    if operation == '1':
        while (currency := input("Enter the currency you want to convert (USD, EUR, PLN): ").upper()) not in option:
            print("Invalid currency. Try USD, EUR or PLN")

        list = listAndState()

        amount = getFloatAmount()
                
        convert = amount * list[currency]
        print(f"\t{amount} {currency} \n\t{convert} UAH")
    elif operation == '2':
        while (currency := input("Enter the currency you want to be converted (USD, EUR, PLN): ").upper()) not in option:
            print("Invalid currency. Try USD, EUR or PLN")

        list = listAndState()

        amount = getFloatAmount()
                
        convert = amount / list[currency]
        print(f"\t{amount} UAH \n\t{convert} {currency}")
    elif operation == "Quit" or operation == "quit":
        print("Quiting the program...")
        break
    else:
        print("If you want to convert UAH to USD, EUR, PLN - type '1'\nIf you want to convert USD, EUR, PLN to UAH - type '2'\n\tOption: ")