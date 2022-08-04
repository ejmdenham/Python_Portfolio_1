import random
from turtle import Turtle as t, Screen

red = t()
orange = t()
yellow = t()
green = t()
blue = t()

turtles = [red, orange, yellow, green, blue]
t_colors = ["red", "orange", "yellow", "green", "blue"]
screen = Screen()

bet = screen.textinput(title="Make your bets, folks!", prompt="Which turtle is taking home the gold? ")

for i, t in enumerate(turtles):
    t.penup()
    t.color(t_colors[i])
    t.shape("turtle")
    t.goto(-250, -180 + i * 80)


race = True

while race:
    for i, t in enumerate(turtles):
        t.forward(random.randint(5, 15))
        if t.xcor() > 220:
            if t.color()[0] == bet:
                print("winner")
                
            else:
                print("loser")

            race = False

screen.exitonclick()
