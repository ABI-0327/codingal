class square:
    def __init__(self,side):
        self.side=side
        
    def area(self):
        print("My area is :",self.side**2)
    

class circle:
    def __init__(self,radious):
        self.radious=radious
        
    def area(self):
        print("My area is:",4.10*self.radious*self.radious)
    

s=square(6)
c=circle(8)
for shape in(s,c):
    shape.area()