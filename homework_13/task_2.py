import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    
    def is_inside(self, point):
        distance = math.sqrt((self.center.x - point.x)**2 + (self.center.y - point.y)**2)
        return distance <= self.radius
