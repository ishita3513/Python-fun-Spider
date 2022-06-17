import turtle as t 
import colorsys
t.bgcolor('black')
t.tracer(2)
h=0.3
t.hideturtle()
def vastCoding():
    global h
    for i in range(4):
        color=colorsys.hsv_to_rgb(h,1,1)
        h+=0.010
        t.pencolor(color)
        t.fd(200)
        t.right(90)
for j in range(180):
    vastCoding()
    t.goto(0,0)
    t.rt(2)
# t.exitonclick()
