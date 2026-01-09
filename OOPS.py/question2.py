

## Class Method and Self Parameter in Python

class Car: # defining a class
   def __init__(self,brand,model): # constructor
       self.brand =  brand # attribute
       self.model = model # attribute

   def full_name(self):  # class method
        return f"{self.brand} {self.model}"  # using self to access attributes





my_car = Car("toyota","corolla")# creating an object of the class Car
#   print(my_car.brand) # accessing the brand attribute
#   print(my_car.model)
print(my_car.full_name())  # calling the class method


