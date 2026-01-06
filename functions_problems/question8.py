
## Function with **Kwargs
## create a function that accepts any number of keywords argumentsand prints them in the format key : value .

def print_kwargs(**kwargs): ## two asterisks are used to take multiple keyword arguments and single asterisk is used to take multiple positional arguments
    for key, values in kwargs.items():## iterating through the dictionary items
        print(f"{key} : {values}") ## printing key and value in the desired format
        
print_kwargs(name="Alice", age=30, city="New York")  # Example call to the function
print_kwargs(fruit="Apple", color="Red", quantity=5)  # Another example call to the function