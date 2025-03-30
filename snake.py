from turtle import Turtle

# Constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self, color="white"):
        self.segments = []
        self.snake_color = color
        self.is_glowing = False
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Initialize the snake with starting segments."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a single segment to the snake at the specified position."""
        segment = Turtle("square")
        segment.color(self.snake_color)
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        """Extend the snake by one segment."""
        self.add_segment(self.segments[-1].position())
        if self.is_glowing:
            self.set_glow()

    def move(self):
        """Move the snake forward, shifting all segments."""
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # === Direction Handlers ===
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # === Visual Effects ===
    def set_glow(self):
        """Make the snake glow gold (special mode)."""
        self.is_glowing = True
        for segment in self.segments:
            segment.color("gold")

    def reset_color(self):
        """Reset the snake color after special mode ends."""
        self.is_glowing = False
        for segment in self.segments:
            segment.color(self.snake_color)
