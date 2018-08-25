class Square():
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self.s1)
        

x_square = Square(4)
y_square = Square(5)

print(Square.square_list)
