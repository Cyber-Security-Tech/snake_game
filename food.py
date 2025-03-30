from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, color="deepskyblue"):
        super().__init__()
        self.shape("triangle")
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.penup()
        self.color(color)
        self.speed("fastest")
        self.setheading(45)
        self.refresh()  # Place the food randomly when initialized

    def refresh(self):
        """Move the food to a new random location on the screen."""
        x = random.randint(-260, 260)
        y = random.randint(-260, 260)
        self.goto(x, y)

