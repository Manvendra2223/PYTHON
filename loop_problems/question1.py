
## Counting positive numbers :

numbers = [12, -7, 5, 64, -14]
positive_number_count = 0
for num in numbers: ## num is variable that takes each value from the list one by one
    if num> 0:
        positive_number_count += 1
print("Count of positive numbers:", positive_number_count)