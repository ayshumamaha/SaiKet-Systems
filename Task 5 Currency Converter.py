print("===== CURRENCY CONVERTER =====")

print("1 USD = 83 INR")
print("1 EUR = 90 INR")
print("1 GBP = 105 INR")

currency = input("Enter currency (USD/EUR/GBP): ").upper()

amount = float(input("Enter amount: "))

if currency == "USD":
    result = amount * 83
    print(f"{amount} USD = {result} INR")

elif currency == "EUR":
    result = amount * 90
    print(f"{amount} EUR = {result} INR")

elif currency == "GBP":
    result = amount * 105
    print(f"{amount} GBP = {result} INR")

else:
    print("Invalid currency.")
    
