import requests

response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json")
data = response.json()

option = ["USD", "EUR", "PLN"]
while (currency := input("Enter the currency you want to convert (USD, EUR, PLN): ").upper()) not in option:
    print("Invalid currency. Try USD, EUR or PLN")

list = {elem["cc"]: elem["rate"] for elem in data}
print(f"Current state of UAH to {currency} is {list[currency]}")

while True:
    try:
        amount = float(input("Amount to calculate: "))
        break
    except ValueError:
        print("Use numbers for amount.")
        
convert = amount * list[currency]
print(f"\t{amount} {currency} \n\t{convert} UAH")