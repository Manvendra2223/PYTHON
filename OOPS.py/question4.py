
##  Encapsulation in Python

## Modify the car classs to encapsulate the brand attribute , making it private and provide a getter method for it .
 
class Car: # defining a class
   def __init__(self,brand,model): # constructor
       self.__brand =  brand # attribute
       self.model = model # attribute
   def chai_brand(self):  # getter method for brand
        return self.__brand + " ! "
    
    
   def full_name(self):  # class method
        return f"{self.__brand} {self.model}"  # using self to access attributes
 
 
 
class ElectricCar(Car):  # defining a subclass that inherits from Car
    def __init__(self,brand,model,battery_size):  # constructor
        super().__init__(brand,model)  # calling the constructor of the parent class
        self.battery_size = battery_size # additional attribute
        
my_tesla = ElectricCar("tesla","model s",100) # creating an object of the ElectricCar class
# print(my_tesla.__brand)  # calling the inherited class method
print(my_tesla.chai_brand())  # accessing the brand using getter method

## __ makes the attribute private