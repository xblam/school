import numpy as np

class Circle:
    radius = 0
    def print(self):
        return f'circle: rad: {self.radius}'

class Coord(Circle):
    x = 1
    y = 2
    def print(self):
        return f'cordcirrcle: radius {self.radius}, x = {self.x}, y = {self.y}'

class SmartCircle(Coord):
    def magnitude(self):
        return (self.x**2 + self.y**2)**(1/2)
c = Circle()
print(c.print())
cc = Coord()
print(cc.print())
s = SmartCircle()

print(s.magnitude())

# print(super(Coord,cc).print())

c = Circle()


g = set()
g.append(1)