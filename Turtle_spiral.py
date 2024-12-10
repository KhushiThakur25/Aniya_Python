import turtle

screen = turtle.Screen()

screen.bgcolor("black")

t = turtle.Turtle()
t.shape("turtle")
t.color("yellow")

t.speed(10)

for i in range(20):
    t.forward(i*10)
    t.left(45)

t.hideturtle()
screen.exitonclick()