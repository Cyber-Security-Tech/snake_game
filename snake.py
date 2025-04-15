"""
snake.py – Defines the Snake class for SNAKE.EXE.

Handles the creation, movement, growth, direction control, and visual effects
for the snake object in the game.
"""

from turtle import Turtle

# === Constants ===
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# === Snake Class ===
class Snake:
    def __init__(self, color="white"):
        """Initialize the snake with a given color and starting position."""
        self.segments = []
        self.snake_color = color
        self.is_glowing = False
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the initial snake with 3 segments."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds a new segment at the specified position."""
        segment = Turtle("square")
        segment.color(self.snake_color)
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        """Extends the snake by one segment at the tail."""
        self.add_segment(self.segments[-1].position())
        if self.is_glowing:
            self.set_glow()  # Ensure new segment glows too

    def move(self):
        """Moves the snake forward by shifting each segment to the previous one’s position."""
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # === Direction Handlers ===
    def up(self):
        """Change direction to up (unless currently moving down)."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change direction to down (unless currently moving up)."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change direction to left (unless currently moving right)."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change direction to right (unless currently moving left)."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # === Visual Effects ===
    def set_glow(self):
        """Make the snake glow gold (activated during special mode)."""
        self.is_glowing = True
        for segment in self.segments:
            segment.color("gold")

    def reset_color(self):
        """Revert the snake’s color to the original after special mode ends."""
        self.is_glowing = False
        for segment in self.segments:
            segment.color(self.snake_color)
