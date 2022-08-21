from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        x_cordinate = random.randint(-280, 280)
        y_cordinate = random.randint(-280, 280)
        self.goto(x_cordinate, y_cordinate)
