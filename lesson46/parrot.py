class parrot:
    specices="Bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sing(self,song):
        print("she sings the song",song)
obj=parrot("Eli",2)
print("It is a",obj.specices)
print("It's name is", obj.name)
print("She is",obj.age)
print(obj.sing("happy"))
