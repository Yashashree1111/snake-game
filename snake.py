from turtle import Turtle, Screen
import time

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]

    def make_snake(self):
        for pos in POSITION:
            self.add_segment(pos)

    def add_segment(self, pos):
        turtle = Turtle(shape="square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(pos)
        self.segments.append(turtle)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def move(self):

        for i in range(len(self.segments) - 1, 0, -1):
            x_cordinate = self.segments[i - 1].xcor()
            y_cordinate = self.segments[i - 1].ycor()
            self.segments[i].goto(x_cordinate, y_cordinate)

        self.head.forward(MOVE_FORWARD)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)
