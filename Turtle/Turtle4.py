import random
import turtle
from turtle import Turtle as t, Screen

d = int(input("distance: "))
tim = t()
tim.shape("turtle")
turtle.colormode(255)
tim.pensize(10)
tim.speed(0)
screen = Screen()
direction = [0, 90, 180, 270]


def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)

    return random_color


def rand_walk():
    tim.color(rand_color())
    tim.forward(30)  # random.randint(20, 35)
    tim.setheading(random.choice(direction))


for _ in range(d):
    rand_walk()

screen.exitonclick()
