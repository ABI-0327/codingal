import turtle

#creating canvas
screen=turtle.Screen()

screen.bgcolor("Lavender")
screen.setup(600,400)

turtle.title("welcome to python canvas.")

hero=turtle.Turtle()
#creating star
for i in range(3):
    hero.forward(100)
    hero.left(120)

hero.penup()
hero.left(90)
hero.forward(50)
hero.right(90)
for i in range(3):
    hero.pendown()
    hero.forward(100)
    hero.right(120)

turtle.done()


