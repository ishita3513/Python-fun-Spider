from tkinter import N
import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(0)
n=36
h=0
for i in range(80):
    c=colorsys.hsv_to_rgb(h,8,0.7)
    h+=1/n 
    t.color(c)
    t.left(5)
