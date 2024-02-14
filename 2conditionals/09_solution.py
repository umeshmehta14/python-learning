year = int(input("Enter Year"))

if (year % 400 == 0) or (year%100 != 0 and year %4 == 0):
    print(year , " Is Leap Year")
else:
    print(year , " Is Not Leap Year")
