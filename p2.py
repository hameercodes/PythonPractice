#Write a class Circle with a method to compute area and perimeter given a radius.
class Circle:
    pi = 3.14 #class attributes
    def __init__(self,r):
        self.redius = r #object attributes
    
    def area(self):
        self.ar = self.redius * self.redius * self.pi 
        print("Area is", self.ar)
    
    def perimeter(self):
        self.peri = 2 * self.pi * self.pi
        print("perimeter is", self.peri)
r1 = Circle(5)
r1.area()
r1.perimeter()