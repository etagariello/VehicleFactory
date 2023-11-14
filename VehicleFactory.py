import random
import Vehicles

class VehicleFactory:
    @staticmethod
    def create_vehicle():
        vehicle_type = random.choice(['Car', 'Truck', 'Boat'])
        make = random.choice(['Ford', 'Toyota', 'Honda'])
        model = 'ModelX'  # Simplified for this example
        year = random.randint(1990, 2022)
        weight = random.randint(1000, 3000)
        num_doors = random.randint(2, 5)
        payload_capacity = random.randint(3000, 9000)
        length = random.randint(10, 50)

        obj = None
        if vehicle_type == 'Car':
            obj = Vehicles.Car(make, model, year, weight, num_doors)
        if vehicle_type == 'Truck':
            obj = Vehicles.Truck(make, model, year, weight, num_doors, payload_capacity)
        if vehicle_type == 'Boat':
            obj = Vehicles.Boat(make, model, year, weight, num_doors, length)
        return obj
    # Return the vehicle.


def process_vehicles(vehicle_list):
    # for each Car, Boat or other, print its contents and make it honk
    for vehicle in vehicle_list:
        print(f"------------------------------\n{vehicle}\n{vehicle.honk()}\n------------------------------")


# Testing
vehicle_list = [VehicleFactory.create_vehicle() for _ in
                range(5)]  # <- what does this do? It makes a list is what it does
process_vehicles(vehicle_list)
