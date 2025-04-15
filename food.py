"""
food.py – Defines the Food class for SNAKE.EXE.

Handles the creation, styling, and repositioning of food items on the screen.
"""

from turtle import Turtle
import random

# === Food Class ===
class Food(Turtle):
    def __init__(self, color="deepskyblue"):
        """
        Initialize a Food object with given color and shape.
        Automatically places the food at a random location.
        """
        super().__init__()
        self.shape("triangle")
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.penup()
        self.color(color)
        self.speed("fastest")
        self.setheading(45)  # Rotate triangle for a cuter look
        self.refresh()       # Place food at a random location initially

    def refresh(self):
        """Reposition the food to a new random location within bounds."""
        x = random.randint(-260, 260)
        y = random.randint(-260, 260)
        self.goto(x, y)
