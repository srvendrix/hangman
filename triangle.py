class Triangle():
    def __init__(self, x, y):
        self.teihen = x
        self.height = y

    def calculate_area(self):
        return (self.teihen * self.height) / 2

a_triangle = Triangle(5, 8)
print(a_triangle.calculate_area())

