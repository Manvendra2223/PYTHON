
#  Inheritance 

#  Create an ElectricCar class that inherits from the Car class. Add an additional attribute 'battery_size'.


class Car: # defining a class
   def __init__(self,brand,model): # constructor
       self.brand =  brand # attribute
       self.model = model # attribute

   def full_name(self):  # class method
        return f"{self.brand} {self.model}"  # using self to access attributes

class ElectricCar(Car):  # defining a subclass that inherits from Car
    def __init__(self,brand,model,battery_size):  # constructor
        super().__init__(brand,model)  # calling the constructor of the parent class
        self.battery_size = battery_size # additional attribute
        
my_tesla = ElectricCar("tesla","model s",100) # creating an object of the ElectricCar class
print(my_tesla.full_name())  # calling the inherited class method
print(my_tesla.battery_size)  # accessing the additional attribute