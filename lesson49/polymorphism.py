class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("I am a cat.My name is",self.name,"I am ",self.age,"years old.")
    def make_sound(self):
        print("meow")

class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("I am a dog.My name is",self.name,"I am ",self.age,"years old.")
    def make_sound(self):
        print("bark")

c=cat("kittey",2.5)
d=dog("yeontan",3)
for a in(c,d):
    a.make_sound()
    a.info()