

## List Uniqueness Checker 
## This program checks if all elements in a list are unique.if not exit the loop and print the duplicate element.

items = ["apple", "banana", "orange", "apple", "grape"]

unique_items = set()

for item in items:
    if item in unique_items:
        print("Duplicate found:", item)
        break
    unique_items.add(item)

