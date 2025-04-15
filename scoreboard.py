"""
scoreboard.py – Defines the Scoreboard class for SNAKE.EXE.

Handles score tracking, display, special mode status, and game-over UI.
Persists the high score in a local text file between sessions.
"""

from turtle import Turtle
import time
from playsound import playsound

# === Constants ===
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")

# === Scoreboard Class ===
class Scoreboard(Turtle):
    def __init__(self, color="deeppink"):
        """
        Initializes the scoreboard with starting score, high score, and visual setup.
        """
        super().__init__()
        self.score = 0
        self.double_points = False
        self.color(color)
        self.penup()
        self.hideturtle()
        self.goto(0, 240)

        # Load high score from file or initialize to 0
        try:
            with open("high_score.txt") as file:
                self.high_score = int(file.read())
        except (FileNotFoundError, ValueError):
            self.high_score = 0

        self.update_score()

    # === Score Display ===
    def update_score(self):
        """Update the scoreboard display with the current score and high score."""
        self.clear()
        self.goto(0, 240)
        self.write(
            f"SCORE: {self.score}   HIGH SCORE: {self.high_score}",
            align=ALIGNMENT,
            font=FONT
        )

    def increase_score(self):
        """Increases the score by 1 or 2 depending on special mode."""
        self.score += 2 if self.double_points else 1
        self.update_score()

    # === Special Mode Handling ===
    def activate_double_points(self):
        """Enable double points during special mode."""
        self.double_points = True

    def deactivate_double_points(self):
        """Disable double points when special mode ends."""
        self.double_points = False

    def show_special_mode(self, seconds_left):
        """Display special mode countdown in gold text."""
        self.goto(0, 210)
        self.color("gold")
        self.write(
            f"🌟 SPECIAL MODE: {seconds_left}s 🌟",
            align=ALIGNMENT,
            font=("Courier", 18, "bold")
        )
        self.color("deeppink")

    # === Game Over + High Score ===
    def show_new_high_score(self):
        """Flash a celebratory message when a new high score is achieved."""
        playsound("sounds/new_high_score.wav", block=False)
        flash = Turtle()
        flash.hideturtle()
        flash.penup()
        flash.color("gold")
        flash.goto(0, 40)

        for _ in range(6):
            flash.write("🌟 NEW HIGH SCORE! 🌟", align=ALIGNMENT, font=("Courier", 22, "bold"))
            flash.getscreen().update()
            time.sleep(0.2)
            flash.clear()
            flash.getscreen().update()
            time.sleep(0.2)

        flash.write("🌟 NEW HIGH SCORE! 🌟", align=ALIGNMENT, font=("Courier", 22, "bold"))

    def game_over(self):
        """
        Display 'Game Over' and update high score file if necessary.
        Also triggers new high score animation if applicable.
        """
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))
            self.show_new_high_score()

        playsound("sounds/game_over.wav", block=False)
        self.goto(0, -20)
        self.color("purple")
        self.write("✧ GAME OVER ✧", align=ALIGNMENT, font=("Courier", 28, "bold"))
