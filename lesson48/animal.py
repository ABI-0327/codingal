from abc import ABC ,abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    print("i can walk and run")
class snake(animal):
    print("i can throll")
h=human()
h.move()
s=snake()
s.move()

