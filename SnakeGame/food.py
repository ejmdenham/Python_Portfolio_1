import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=.5, stretch_wid=-.5)
        self.refresh()

    def refresh(self):
        self.food_pos = random.randrange(-280, 300, 20), random.randrange(-280, 300, 20)
        self.goto(self.food_pos)
        print("loc is: ", self.food_pos)


