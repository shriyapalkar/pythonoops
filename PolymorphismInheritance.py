#Method Overriding
from math import pi
class Shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        pass
    def fact(self):
        return "I am 2d shape"
    def __str__(self):
        return self.name
class Square(Shape):
    def __init__(self,length):
        super().__init__("square")
        self.length=length
    def area(self):
        return self.length**2
    def fact(self):
        return "squares have each angle equal to 90 degrees"

class Circle(Shape):
    def __init__(self,radius):
        super().__init__("circle")
        self.radius=radius
    def area(self):
        return pi*self.radius**2

s1=Square(2)
c1=Circle(7)
print(c1)
print(c1.fact())
print(s1.fact())
print(s1.area())
print(c1.area())

