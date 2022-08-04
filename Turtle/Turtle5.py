import random
import turtle
from turtle import Turtle as t, Screen

tim = t()
screen = Screen()
turtle.colormode(255)

tim.shape("turtle")
tim.speed(0)


def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)

    return random_color


def draw_spirograph(tightness=5, radius=100):
    for i in range(0, 360, tightness):
        tim.color(rand_color())
        tim.setheading(i)
        tim.circle(radius)


draw_spirograph(10, 100)
screen.exitonclick()
