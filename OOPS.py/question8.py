
# Property Decorators

## Use a property decorator in the car class to make the model attribute read-only.


class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model   # ✅ fixed
        Car.total_car += 1

    def chai_brand(self):
        return self.__brand + " ! "

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Gasoline"

    @staticmethod
    def general_discription():
        return "Cars are mean of transport that run on roads."

    @property
    def model(self):
        return self.__model   # 🔒 read-only


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electricity"


# ---- object creation ----
my_car = Car("Safari", "2024")

# ❌ do NOT modify read-only property
# my_car.model = "City"

print(my_car.model)

