from functools import reduce

numbers = [1, 2, 3, 4, 5]

def square(num):
    return num ** 2

squared_numbers = map(square, numbers)
print(list(squared_numbers))

filter_nums = filter(lambda x: x%2 == 0, numbers)

print(list(filter_nums))

reduced_numbers = reduce(lambda acc, cur: acc + cur, numbers)