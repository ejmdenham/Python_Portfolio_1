import random
from turtle import Turtle as t, Screen

tim = t()
tim.shape("turtle")
screen = Screen()

colors = ["red", "blue", "yellow", "cyan", "magenta", "orange", "green", "silver", "wheat", "chartreuse"]

for i in range(10, 2, -1):
    color = random.choice(colors)
    tim.color(color)
    colors.pop(colors.index(color))
    for _ in range(i):
        tim.forward(100)
        tim.right(360 / i)

screen.exitonclick()
