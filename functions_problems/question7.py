
## Function with *args
## write a function that takes variable number of arguments and returns their sum.

def sum_all(*args): ## if we use chai or any char in place of args it will work the same way but if we remove * it will give error becuase * is used to take multiple arguments
    print(args)  # This will print the tuple of all arguments passed and if we print *args it will print all the arguments separately.
    for i in  args:
        print(i*2)  # printing square of each argument
    return sum(args)

print(sum_all(1, 2, 3, 4))  # Example call to the function
print(sum_all(10, 20))      # Another example call to the function