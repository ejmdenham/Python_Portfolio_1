from cmath import sqrt
from turtle import Turtle, Screen
import numpy as np

color_list = ["red", "blue", "yellow", "cyan", "magenta", "orange", "green", "grey"]

t_turtle = Turtle()
screen = Screen()

t_turtle.shape("turtle")
t_turtle.color("red")


def pythagoras(a):
    return sqrt(2 * a ** 2)


def squarception(x):
    color = []

    for i in range(x):
        color.append(list(np.random.choice(color_list, size=1)))

    s = pythagoras(x)
    c = 0

    for i in range(x, 0, -10):
        for _ in range(0, 4):
            t_turtle.color(color[c])
            t_turtle.right(90)
            t_turtle.forward(i)
            c += 1
    else:
        t_turtle.color(color[c])
        t_turtle.right(90 + 45)
        t_turtle.forward(abs(s))
        t_turtle.right(-90)
        c = 0
        t_turtle.color(color[c])
        t_turtle.circle(abs(s / 2), 360)


for _ in range(8):
    squarception(140)

screen.exitonclick()
