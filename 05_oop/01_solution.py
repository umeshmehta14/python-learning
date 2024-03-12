class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand

    def disp_name(self):
        return f"{self.__brand}: {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Car has 4 tyres"

    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


tesla_car = ElectricCar("Testa", "S", "87kwh")

# print(isinstance(tesla_car, ElectricCar))
# print(isinstance(tesla_car, Car))

# tesla_car.model = "wjshb"

# print(tesla_car.fuel_type())

# safari = Car("My", "CAR")
# print(safari.fuel_type())

# print(Car.total_car)

# print(Car.general_description())

# print(tesla_car.model)

# my_car = Car(brand="Honda", model="Bmw")

# print(my_car.model)
# print(my_car.brand)

# print(my_car.disp_name())


class Battery:
    def battery_info(self):
        return "this is a battery"

class Engine:
    def engine_info(self):
        return "this is a engine"

class New_electric_car(Battery, Engine, Car):
    pass

new_car = New_electric_car("MYBARND", "MODELSSSS")

print(new_car.battery_info())

