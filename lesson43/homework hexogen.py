import turtle

#creating canvas
screen=turtle.Screen()

screen.bgcolor("Lavender")
screen.setup(600,400)

turtle.title("welcome to python canvas.")

hero=turtle.Turtle()
#creating hexogen
for i in range(3):
    hero.forward(90)
    hero.left(60)
    hero.forward(80)
    hero.left(70)
    hero.forward(80)
    hero.left(50)
    hero.forward(80)
    hero.left(60)
    hero.forward(80)
    hero.left(64)
    hero.forward(75)
    hero.left(70)

    hero.penup()
    hero.right(120)
    hero.forward(50)


    

    turtle.done()

    

