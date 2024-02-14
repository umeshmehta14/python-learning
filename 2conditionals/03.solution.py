marks = int(input("Enter marks"))

# if marks > 100:
#     print("Invalid marks")
#     exit()

if marks > 100:
    print("Invalid marks")
elif marks > 90:
    print("A Grade")
elif marks > 80:
    print("B Grade")
elif marks > 70:
    print("C Grade")
elif marks > 60:
    print("D Grade")
else:
    print("F Grade")

