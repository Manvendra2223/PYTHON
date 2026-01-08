
## Basic Class and objects in Python
## Create a class named 'Car' with attributes 'make', 'model', and 'year'.then create instance of the class .


# class is the blueprint. it is a keyword to define a class
## objects are instances of a class


class Car: # defining a class
   def __init__(self,brand,model): # constructor
       self.brand =  brand # attribute
       self.model = model # attribute

my_car = Car("toyota","corolla")# creating an object of the class Car
print(my_car.brand) # accessing the brand attribute
print(my_car.model)

my_new_car = Car("honda","civic") # creating another object of the class Car
print(my_new_car.brand)
print(my_new_car.model)