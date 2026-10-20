class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        return 3.14 * (self.radius ** 2)

radius = float(input("Enter the radius of the circle: "))
print(f"Area of the circle: {Circle(radius=radius).get_area():.2f}")
