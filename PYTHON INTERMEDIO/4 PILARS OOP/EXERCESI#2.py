
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)


circle = Circle(5)
print("Circle Area:", circle.calculate_area())
print("Circle Perimeter:", circle.calculate_perimeter())

Rectangle = Rectangle(4, 6)
print("Rectangle Area:", Rectangle.calculate_area())
print("Rectangle Perimeter:", Rectangle.calculate_perimeter())

square = Square(4)
print("Square Area:", square.calculate_area())
print("Square Perimeter:", square.calculate_perimeter())

