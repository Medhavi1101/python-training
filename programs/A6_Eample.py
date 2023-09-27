import math
class Circle:
    def create(self, radius):
        c = Circle()
        self.radius = radius
        return c 
    
    def is_valid(self):
        return isinstance(self, Circle) and self.radius>0
    
    def perimeter(self):
        return 2 * math.pi * self.radius 
    
    def area(self):
        return math.pi * self.radius* self.radius

    def info(self):
        return f'Circle({self.radius})' 

   
