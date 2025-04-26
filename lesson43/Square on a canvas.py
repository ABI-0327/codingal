import turtle

#creating canvas
screen=turtle.Screen()

screen.bgcolor("Lavender")
screen.setup(600,400)

turtle.title("welcome to python canvas.")

hero=turtle.Turtle()

for i in range(4):
    hero.forward(100)
    hero.left(90)


turtle.done()
