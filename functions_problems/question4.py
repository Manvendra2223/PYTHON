
## Function Returning Multiple Values
## Create a function that returns both the area and circumference of a circle given its radius.

import math  # importing the math module to access mathematical functions and constants

def circle_stats(radius):
    area =  math.pi * radius ** 2
    circumference  = 2 * math.pi * radius
    return area, circumference  # returning both area and circumference as a tuple
 
a , c = circle_stats(5)  # calling the function with radius 5 and unpacking the returned tuple
print("Area:", a, "Circumference:", c)  # printing the area and circumference



