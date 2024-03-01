# Poly - Many  - Object oriented programming (OOP)
# Morphism - Forms

# Method Overloading and Method Overriding

class Shape:
    def area(self):
        print("Area of Shape")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shape1 = Circle(11)
print(shape1.area())

shape2 = Rectangle(5, 4)
print(shape2.area())

shape3 = Shape()
print(shape3.area())
