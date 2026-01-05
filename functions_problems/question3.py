
## Polymorphism in Functions
## Write a function multiply that multiplies 2 numbers , but can also accept and multiply strings.

## polymorphism means "many forms". In Python, polymorphism allows functions to process data of different types through a single interface.

def multiply(p1, p2):  # function that takes two parameters
    return p1 * p2   # returns the product of the two parameters

print(multiply(8,5))
print(multiply("Hi ",3))
print(multiply([1,2],3))

# In the above function, multiply can handle both numbers and strings (and even lists) because of polymorphism.