
## Basic Function Syntax
## Write a function to calculate and return the square of a number.

def square(num):    # these parantesis are used to pass parameters/arguments to the function
    print(num ** 2) # this line calculates the square of the number and prints it
    
    
    
#square(5)         # calling the function with an argument of 5
result = square(7)  # calling the function with an argument of 7 and storing the result
print(result)       # printing the result, which will be None since the function does not return

## we also use return statement to return a value from the function