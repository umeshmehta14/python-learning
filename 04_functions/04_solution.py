import math

def circle_stats(r):
    area = math.pi * r **2
    circumference = 2 * math.pi * r
    return area, circumference

a,c  = circle_stats(2)

# Use string formatting to round to 2 decimal places
print("Area: {:.2f}, Circumference: {:.2f}".format(a, c))


# Use the round() function to round to 2 decimal places
print("Area:", round(a, 2), "Circumference:", round(c, 2))