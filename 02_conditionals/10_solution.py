pet = input("Enter Pet Species")
age = int(input("Enter "+ pet +"'s Age"))

if pet.lower() == "dog" and age < 2:
    print("Puppy Food")
else:
    if pet.lower() == "cat" and age > 5:
        print("Senior Cat Food")
    else:
        print("Invalid Information")

