import turtle
from turtle import Turtle as t, Screen
import Turtle4 as t4

tim = t()
screen = Screen()
turtle.colormode(255)

tim.shape("turtle")

for i in range(360):
    tim.color(t4.rand_color())
    tim.setheading(i)
    tim.circle(100)

screen.exitonclick()