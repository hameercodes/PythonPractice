# Implement a Rectangle class with length and width and methods to calculate area and perimeter.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        print(f"The area of the rectangle is: {self.length*self.width}")
    
    def perimeter(self):
        print(f"The perimeter of the rectangle is: {2*(self.length+self.width)}.")

r1 = Rectangle(25,30)
r1.area()
r1.perimeter()

#encapsulation is binding all information in a object.