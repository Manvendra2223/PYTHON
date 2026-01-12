
# Static Method 
# Add a static method to the car class that returns a general description of a car.

## static method means a method that belongs to the class rather than any specific instance(object) of the class.

class Car: # defining a class
    total_car = 0  # class variable to keep track of number of cars created
    def __init__(self,brand,model): # constructor
       self.__brand =  brand # attribute
       self.model = model # attribute
       Car.total_car += 1  # increment the class variable each time a car is created
       
    def chai_brand(self):  # getter method for brand
        return self.__brand + " ! "
    
    
    def full_name(self):  # class method
        return f"{self.__brand} {self.model}"  # using self to access attributes
   
    def fuel_type(self):  # method to demonstrate polymorphism
        return "Gasoline" # fuel type for regular cars
    
    @staticmethod # this decorator is used to define a static method ## decorator means a special type of function that can modify the behavior of a method or class.
    def general_discription():
        return "Cars are mean of transport that run on roads."
    
class ElectricCar(Car):  # defining a subclass that inherits from Car
    def __init__(self,brand,model,battery_size):  # constructor
        super().__init__(brand,model)  # calling the constructor of the parent class
        self.battery_size = battery_size # additional attribute
        
    def fuel_type(self):  # overriding the method to demonstrate polymorphism
        return "Electricity"
    
my_car = Car("safari","2024") # creating an object of the Car class
Car("safari","2025") # creating another object of the Car class
# print(safari.fuel_type())  # accessing the method to see polymorphism in action

# print(my_car.general_discription())  # accessing the static method to get general description of a car 
print(Car.general_discription())  # accessing the static method using class name