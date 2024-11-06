class Vehicle:
    def __init__(self, type):
         self.type = type

    def description(self):
        return f"Pojazd marki: {self.type}"

class Car(Vehicle):
    def __init__(self, type, model, year):
#         self.type = type
         super().__init__(type)
         self.model = model
         self.year = year

    def description(self):
        return f"{self.type} {self.model} {self.year}"

