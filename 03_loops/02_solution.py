n = int(input("Enter Number"))
sum_even = 0

for i in range(1, n+1):
    if(i%2 == 0):
        sum_even += i

print("Sum Of even numbers are ", sum_even)
