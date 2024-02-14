weather = input("Enter Weather")

if weather.lower() == "sunny":
    print("Go For a Walk")
elif weather.lower() == "rainy":
    print("Read a Book")
elif weather.lower() == "snowy":
    print("build a snowman")
else:
    print("Invalid weather")