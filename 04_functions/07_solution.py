def sum_all(*args):
    for i in args:
        print(i)
    return sum(args)

print(sum_all(1,2,4,5,))