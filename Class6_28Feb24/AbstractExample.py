# Abstract class

# internal working getting hidden and only important details known to world

# Abstract class and Abstract method
# abc -> Abstract base class need to import

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        # Abstract method with no definition
        pass


class Dog(Animal):
    def sound(self):
        return "Bow Bow"


class Cat(Animal):

    def sound(self):
        return "Meow Meow"


dog = Dog("Bruno")
print(dog.sound())

cat = Cat("Selina")
print(cat.sound())
