

## Validate Input 
## keep asking the user for a number between 1 and 10 until they provide a valid input.

while True:
    number = int(input("Enter value b/w 1 and 10: "))
    if 1 <= number <= 10:
        print("Valid input received:", number)
        break
    else:
        print("Invalid input. Please try again.")