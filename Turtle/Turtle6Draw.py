import turtle as t

tim = t.Turtle()
screen = t.Screen()


def go_forward():
    tim.forward(10)


def go_back():
    tim.bk(10)


def turn_left():
    tim.left(5)


def turn_right():
    tim.right(5)


screen.listen()

screen.onkey(key="w", fun=go_forward)
screen.onkey(key="s", fun=go_back)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=screen.reset)


screen.exitonclick()
