age = int(input("enter age"))
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2

print("Price for your ticker is $",price)