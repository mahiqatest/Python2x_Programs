# Hierarchical Inheritance

class Vehicle:
    def info(self):
        return "This is vehicle"


class Car(Vehicle):
    def info(self):
        return "This is car"


class Bicycle(Vehicle):
    def info(self):
        return "This is bicycle"


car = Car()
royale_enfield = Bicycle()
tempo = Vehicle()

print(car.info())
print(royale_enfield.info())
print(tempo.info())
