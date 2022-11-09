from turtle import Turtle
import random

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("circle")
        segment.color(random.choice(["white", "red"]))
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        # Add a new segment to the snake.
        self.add_segment(self.segments[-1].position())

    def move(self):
        for turt in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[turt - 1].xcor()
            new_y = self.segments[turt - 1].ycor()
            self.segments[turt].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)