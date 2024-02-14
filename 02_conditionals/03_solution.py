fruit = "Banana"
color = input("Enter color of banana")

if fruit == "Banana":
    if color.lower() == "green":
        print("Unripe")
    elif color.lower() == "yellow":
        print("Ripe")
    elif color.lower() == "Brown":
        print("Overripe")
    else:
        print("Unknown color")
else:
    print("Invalid Fruit")