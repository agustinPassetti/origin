# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.

class Rectangle ():
    def __init__(self, l, w):
        self.rect_l = l
        self.rect_w = w    
    """def length(self) :
        self.rect_l = input ("What is the length of your rectangle? ")
    def width(self) :
        self.rect_w = input ("What is the width of your rectangle? ")"""
    def area  (self):
        #area = self.rect_l * self.rect_w
        #print(self.rect_l * self.rect_w)
        return self.rect_l * self.rect_w
rect1 = Rectangle(12, 10)
print(rect1.area())

