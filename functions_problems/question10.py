
## Recursive Function 
## Create  a recursive function to calculate the factorial of a number.

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)  ## base case is when n is 0, factorial of 0 is 1
    
print(factorial(5))  ## calling the function to calculate factorial of 5
print(factorial(0))  ## calling the function to calculate factorial of 0