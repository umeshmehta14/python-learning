items = ["apple", "banana", "orange", "apple", "mango"]

unique_items = set()

for item in items:
    if item in unique_items:
        print("Duplicate item is ", item)
        break
    else:
        unique_items.add(item)
