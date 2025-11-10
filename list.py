tea_var = ["green", "black", "herbal"]
coffee_var = ["espresso", "latte", "cappuccino"]
print("Available tea varieties:", tea_var)
print("Available coffee varieties:", coffee_var)
all_varieties = tea_var + coffee_var
print("All available varieties:", all_varieties)
print("Total number of varieties:", len(all_varieties))
print("First variety:", all_varieties[0])
print("Last variety:", all_varieties[-1])
print("Varieties from index 2 to 4:", all_varieties[2:5])
print("Varieties from index 3 to end:", all_varieties[3:])
print("Varieties from start to index 3:", all_varieties[:4])
# This code defines two lists of beverage varieties, combines them, and performs various operations to display information about the combined list.
tea_var[1:2] = ["white"]
print("Updated tea varieties:", tea_var)
tea_var.append("oolong")
print("Tea varieties after appending:", tea_var)
print("Number of tea varieties:", len(tea_var))
tea_var.insert(1, "chamomile")
print("Tea varieties after insertion:", tea_var)
tea_var.remove("herbal")
print("Tea varieties after removal:", tea_var)
print("Final tea varieties:", tea_var)
print("Final coffee varieties:", coffee_var)
# The code also demonstrates how to modify the tea varieties list by replacing, appending, inserting, and removing items, while displaying the list after each operation.
for variety in all_varieties:
    print("Enjoy your", variety + "!")
    print(tea_var,end=" ")
    if "green" in tea_var:
        print("Green tea is available.")
print("Iterating through all varieties:")
# Finally, the code iterates through all beverage varieties, printing a message for each, and
if "espresso" in coffee_var:
    print("Espresso is available.") #checks for the presence of specific varieties in the tea and coffee lists.
if "black" in tea_var:
 print("Black tea is available.")
 

