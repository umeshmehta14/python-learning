n = int(input("Enter Number"))
fact = 1

while n > 0:
    fact *= n
    n -= 1

print("Factorial is ", fact)
