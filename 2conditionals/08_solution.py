password = input("Enter Your Password")
password_length = len(password)

if password_length < 6:
    print("Weak")
elif password_length <= 10:
    print("Medium")
else:
    print("Strong")