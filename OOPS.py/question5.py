
##  Polymorphism 

## means "many forms" and it occurs when we have many classes that are related to each other by inheritance.

## demonstrate polymorphism by difining a method fuel_type in both Car and ElectricCar classes, but with different behaviours.

class Car: # defining a class
   def __init__(self,brand,model): # constructor
       self.__brand =  brand # attribute
       self.model = model # attribute
   def chai_brand(self):  # getter method for brand
        return self.__brand + " ! "
    
    
   def full_name(self):  # class method
        return f"{self.__brand} {self.model}"  # using self to access attributes
   
   def fuel_type(self):  # method to demonstrate polymorphism
        return "Gasoline" # fuel type for regular cars
 
 
class ElectricCar(Car):  # defining a subclass that inherits from Car
    def __init__(self,brand,model,battery_size):  # constructor
        super().__init__(brand,model)  # calling the constructor of the parent class
        self.battery_size = battery_size # additional attribute
        
    def fuel_type(self):  # overriding the method to demonstrate polymorphism
        return "Electricity"
    
    
my_tesla = ElectricCar("tesla","model s",100) # creating an object of the ElectricCar class
# print(my_tesla.__brand)  # calling the inherited class method
print(my_tesla.fuel_type())  # accessing the overridden method to see polymorphism in action

safari = Car("safari","2024") # creating an object of the Car class
print(safari.fuel_type())  # accessing the method to see polymorphism in action