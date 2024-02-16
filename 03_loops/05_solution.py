input_str = input("Enter String")

for char in input_str:
    if input_str.count(char) == 1:
        print("The First Non Repeated Character is : ", char)
        break
