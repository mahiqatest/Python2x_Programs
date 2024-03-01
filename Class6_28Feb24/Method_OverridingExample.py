class Animal:

    def __init__(self):
        pass

    def sound(self):
        print("animal sound")


class Dog(Animal):
    def __init__(self):
        super().__init__()

    def sound(self):
        super().sound() # call to parent method
        print("Dog sound")


bruno = Dog()
bruno.sound()
