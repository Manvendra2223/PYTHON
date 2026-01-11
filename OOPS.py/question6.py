
 # class variables 
 ## add a class variable to car that keeps track of the number of cars created.
 
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
 
 
class ElectricCar(Car):  # defining a subclass that inherits from Car
    def __init__(self,brand,model,battery_size):  # constructor
        super().__init__(brand,model)  # calling the constructor of the parent class
        self.battery_size = battery_size # additional attribute
        
    def fuel_type(self):  # overriding the method to demonstrate polymorphism
        return "Electricity"
    
    
# my_tesla = ElectricCar("tesla","model s",100) # creating an object of the ElectricCar class
# print(my_tesla.__brand)  # calling the inherited class method
# print(my_tesla.fuel_type())  # accessing the overridden method to see polymorphism in action

Car("safari","2024") # creating an object of the Car class
Car("safari","2025") # creating another object of the Car class
# print(safari.fuel_type())  # accessing the method to see polymorphism in action
print("Total cars created:", Car.total_car)  # accessing the class variable to see total cars created