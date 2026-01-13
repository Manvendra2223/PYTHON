
## Multiple inheritance 

 # create two classes Battery and Engine and let the ElectricCar inherit from both, demonstrating multiple inheritance.
 
## multiple inheritance means a class can inherit attributes and methods from more than one parent class.

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
      
       
     
class Battery:
      def battery_info(self):
       return "This car has a battery size of {self.battery_size} kWh"

class Engine:
      def engine_info(self):
         return "This car has an electric engine"

class ElectricCar(Battery,Engine):  # defining a subclass that inherits from Car, Battery, and Engine
      pass

my_new_tesla = ElectricCar()  # creating an instance of ElectricCar
print(my_new_tesla.engine_info())  # calling the inherited method from Car
print(my_new_tesla.battery_info())  # calling the inherited method from Battery