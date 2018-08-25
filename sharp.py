class Shape():
    def what_am_i(self):
        print('I am a shape')
        

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.len = length

    def calculate_perimeter(self):
        return self.width * 2 + self.len * 2

class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, s2):
        self.s1 += s2

a_rectangle = Rectangle(30, 30)
print(a_rectangle.what_am_i())

print(a_rectangle.calculate_perimeter())

