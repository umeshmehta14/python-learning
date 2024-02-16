number = int(input("Enter number"))

is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i == 0):
            is_prime = False
            break
else:
    print("Number must be greater than 1")

if is_prime:
    print("Number is prime")
else:
    print("Number is not prime")