
#  Timing Function Execution 

# write a decorator that measures the time a function takes to execute .

import time # import time module to measure execution time

def timer(func):# decorator function
    def wrapper(*args, **kwargs): # wrapper function to wrap around the original function
        start_time = time.time() # record start time
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time}")
        return result # return the result of the original function
    return wrapper # return the wrapper function

@timer # apply the decorator to a sample function
def example_function(n): # sample function to demonstrate the decorator
    time.sleep(n)
    
example_function(2) # call the decorated function with a sleep time of 2 seconds
        
                               