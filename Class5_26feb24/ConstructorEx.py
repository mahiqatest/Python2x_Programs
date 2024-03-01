class Car:
    name = None
    make = None
    model = None

    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Name of car: " +self.name)
        print("Make of car: " +self.make)
        print("Model of car: " +self.model)

lambo = Car("Lambo","V2","2023")
audi = Car("Audi","V3", "2022")

lambo.start_engine()
audi.start_engine()