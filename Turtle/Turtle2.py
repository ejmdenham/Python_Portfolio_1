from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.shape("turtle")
tim.color("red")


def dashed_line(linelen, spacelen=10, dashlen=10):
    length = 0

    while length <= linelen:
        if length <= linelen:
            tim.forward(dashlen)
            tim.penup()
            length += dashlen
        if length <= linelen:
            tim.forward(spacelen)
            tim.pendown()
            length += spacelen

    print(length)


dashed_line(150)

screen.exitonclick()
