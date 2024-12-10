import turtle

screen = turtle.Screen()

screen.bgcolor("Lightblue")
#Set the background color of the window
#create a turtle
t = turtle.Turtle()
t.shape('turtle')
t.color("green")

for _ in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.setposition(-150,0)
t.pendown()

t.color("red")
t.circle(30)

screen.exitonclick()