class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight

    def __str__(self):
        return f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nWeight: {self.weight}"

    def __repr__(self):
        return f"Vehicle({self.make!r}, {self.model!r}, {self.year!r}, {self.weight!r})"

    def honk(self):
        return "Honk!"


# Dunder functions here

class Car(Vehicle):
    def __init__(self, make, model, year, weight, num_doors):
        super().__init__(make, model, year, weight)
        self.num_doors = num_doors

    # Add class specific attributes and __str__, __repr__ methods here
    def __str__(self):
        return f"A car has been made:\n{super().__str__()}\nNum Doors: {self.num_doors}"

    def __repr__(self):
        return f"Car({self.make!r}, {self.model!r}, {self.year!r}, {self.weight!r}, {self.num_doors!r})"

    def honk(self):
        return "Beep beep!"


class Truck(Vehicle):
    def __init__(self, make, model, year, weight, num_doors, payload_capacity):
        super().__init__(make, model, year, weight)
        self.payload_capacity = payload_capacity
        self.num_doors = num_doors

    # Add class specific attributes and __str__, __repr__ methods here
    def __str__(self):
        return f"A truck has been made:\n{super().__str__()}\nNumber of doors: {self.num_doors}\nPayload capacity: {self.payload_capacity}"

    def __repr__(self):
        return f"Truck({self.make!r}, {self.model!r}, {self.year!r}, {self.weight!r}, {self.payload_capacity!r})"

    def honk(self):
        return "Honk honk!"


class Boat(Vehicle):
    def __init__(self, make, model, year, weight, num_doors,  length):
        super().__init__(make, model, year, weight)
        self.length = length
        self.num_doors = num_doors

    # Add class specific attributes and __str__, __repr__ methods here
    def __str__(self):
        return f"A boat has been made:\n{super().__str__()}\nNumber of doors: {self.num_doors}\nLength: {self.length}"

    def __repr__(self):
        return f"Boat({self.make!r}, {self.model!r}, {self.year!r}, {self.weight!r}, {self.length!r})"

    def honk(self):
        return "TOOT TOOT!"