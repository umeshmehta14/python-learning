age = int(input("enter age : "))

if age < 13:
    print("child")
elif age < 20:
    print("teenager")
elif age < 60:
    print("adult")
else:
    print("senior")