file = open("test.py", 'w')


try:
    file.write("Hello this is umesh")
finally:
    file.close()

with open("test.py", 'w') as file:
    file.write("Hello this is umesh mehta")