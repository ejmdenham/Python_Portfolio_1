import random
import turtle

tim = turtle.Turtle()
tim.penup()
screen = turtle.Screen()
turtle.colormode(255)
tim.hideturtle()
tim.speed(0)


def rand_color():
    r = random.randint(30, 250)
    g = random.randint(15, 215)
    b = random.randint(0, 230)
    random_color = (r, g, b)

    return random_color


def draw_spirograph(color, tightness=5, radius=100.0):
    for degree in range(0, 360 + tightness, tightness):
        tim.pendown()
        tim.color(color)
        tim.setheading(degree)
        tim.circle(radius)
        tim.penup()


x_0 = -225
y_0 = -225

for i in range(10):
    # set origin to (x_0, y_0)
    tim.goto(x_0, y_0 + 50 * i)
    for j in range(10):
        # dot of size 20 and color ?
        new_color = rand_color()
        draw_spirograph(new_color, 30, 12.5)
        tim.dot(20, new_color)
        # move 50
        tim.forward(50)

canvas = screen.getcanvas()

canvas.postscript(file="Spirohirst1.eps", x=-300, y=-300, width=600, height=600)

screen.exitonclick()
