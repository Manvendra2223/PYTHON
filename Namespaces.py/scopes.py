
## Scopes in Python




username = "mannu" # Global scope

## local scope example 
def greet():
    username = "john" # Local scope
    print("Hello, " + username)
greet()  # Output: Hello, john
print("Global username: " + username)  # Output: Global username: mannu


x = 99  # Global scope

# def func2(y): # Local scope
    # z = x + y
    # return z

# result = func2(1) 
# print(result)


# def func3():
    # global x # Declare x as global
    # x = 100  # Modify the global variable
# func3()
# print("Inside func3, x =", x)


def f1(): # Enclosing scope
    x = 88
    def f2(): # Local scope
        print(x)  # Accessing x from the enclosing scope (f1)
    return f2 # Returning the inner function
my_func = f1() # my_func now holds the inner function f2
my_func()  # Output: 88


def chaicoder(num): # Enclosing scope
    def actual(x): # Local scope
        return x ** num # Using num from the enclosing scope
    return actual # Returning the inner function


# def chaicoder(2): # Creating a function that squares a number
    # def actual(x): # Local scope
        # return x ** 2 # Squaring the input
    # return actual # Returning the inner function



f = chaicoder(2) # Creating a function that squares a number
g = chaicoder(3)# Creating a function that cubes a number
print(f(5))  # Output: 25
print(g(5))  # Output: 125