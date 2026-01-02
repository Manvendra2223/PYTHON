
## Find the First Non Repeated Character in a String:

input_str = "swiss"

for char in input_str:
    print(char)
    if input_str.count(char) == 1: ## Check if the character is non-repeated
        print("First Non Repeated Character:", char)
        break ## Exit loop after finding the first non-repeated character