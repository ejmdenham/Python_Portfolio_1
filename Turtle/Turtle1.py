import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.shape("turtle")
tim.color("red")

for _ in range(4):
    tim.right(90)
    tim.forward(100)

screen.exitonclick()
