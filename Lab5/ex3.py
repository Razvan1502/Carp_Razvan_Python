class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency, towing_capacity):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency  # L/100km
        self.towing_capacity = towing_capacity  # KG

    def calculate_mileage(self, distance):
        return (distance * self.fuel_efficiency) / 100

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency,towing_capacity):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency  # L/100km
        self.towing_capacity = towing_capacity  # KG

    def calculate_mileage(self, distance):
        return (distance*self.fuel_efficiency)/100 # L/100km

    def calculate_towing_capacity(self):
        return self.towing_capacity
class Truck(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency, towing_capacity):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency
        self.towing_capacity = towing_capacity

    def calculate_mileage(self, distance):
        return (distance*self.fuel_efficiency)/100


    def calculate_towing_capacity(self):
        return self.towing_capacity


car = Car(make="Audi", model="A5", year=2023, fuel_efficiency=10, towing_capacity= 1000)
motorcycle = Motorcycle(make="Kawasaki ", model="Ninja 400", year=2023, fuel_efficiency=7, towing_capacity=200)
truck = Truck(make="Ford", model="Raptor", year=2023,fuel_efficiency=15 ,  towing_capacity=3000)

car.display_info()
print(f"Car Mileage for 200 km: {car.calculate_mileage(200)} L")

motorcycle.display_info()
print(f"Motorcycle Mileage for 200 km: {motorcycle.calculate_mileage(200)} L")

truck.display_info()
print(f"Truck Mileage for 200 km: {truck.calculate_mileage(200)} L")
print(f"Truck Towing Capacity: {truck.calculate_towing_capacity()} kg")