class geomateryshapes():
    def __init__(self,name,category):
        self.name=name
        self.category=category
    def display(self):
        print(self.name)
        print(self.category)


class shape(geomateryshapes):
    def __init__(self,name,category,sides,lines):
        self.lines=lines
        self.sides=sides



    geomateryshapes.__init__(self,name,category)

obj=shape("square","2D")
obj.display()