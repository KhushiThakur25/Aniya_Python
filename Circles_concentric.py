import turtle

screen = turtle.Screen()

screen.bgcolor("black")

t = turtle.Turtle()
t.shape("turtle")
t.speed(10)
colors = ["red","blue","green","yellow","orange","pink"]

for r in range(50,100,10):
    t.penup()
    t.goto(0,-r)
    t.pendown()
    t.color(colors[r // 10 %len(colors)])
    t.circle(r)

screen.exitonclick()