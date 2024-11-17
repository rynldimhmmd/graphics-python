import turtle

t = turtle.Turtle()

t.speed(0)
t.pensize(2)
t.hideturtle()
turtle.bgcolor("black")

golden_angle = 137.5

distance = 20

angle = 0
t.penup()
t.goto(0, 0)
t.pendown()

for i in range(500):
    t.forward(distance)
    t.right(golden_angle)
    distance += 1
    t.pencolor("gold")

turtle.done()
