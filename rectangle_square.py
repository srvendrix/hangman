class Rectangle():
    def __init__(self, width, length):
        self.width = width
        self.len = length

    def calculate_perimeter(self):
        return self.width * 2 + self.len * 2

class Square():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, s2):
        self.s1 += s2

a_rectangle = Rectangle(25, 50)
a_square = Square(20)

print(a_rectangle.calculate_perimeter())
print(a_square.calculate_perimeter())

a_square = Square(100)
print(a_square.s1)

a_square.change_size(200)
print(a_square.s1)


        
    
