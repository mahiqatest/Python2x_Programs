from abc import ABC, abstractmethod


class Person:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def play_guitar(self):
        pass


class Guitarist(Person):
    def play_guitar(self):
        return "I can play guitar"


person1 = Guitarist("tony")
print(person1.play_guitar())
