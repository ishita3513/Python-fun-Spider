import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.pencolor('orange')
t.speed(0)

for i in range(180):
    t.circle(i,50)
    t.left(90)
    t.circle(180+i,90)
    t.left(18)

# t.exitonclick()
turtle.done()