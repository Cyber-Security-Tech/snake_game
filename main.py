from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import random
from playsound import playsound
import pygame

# === Initialize Pygame for background music ===
pygame.mixer.init()

# === Global Music Control ===
def play_sound(filename):
    playsound(f"sounds/{filename}", block=False)

def play_menu_music():
    pygame.mixer.music.load("sounds/menu_theme.mp3")
    pygame.mixer.music.play(-1)

def play_game_music():
    pygame.mixer.music.load("sounds/game_theme.wav")
    pygame.mixer.music.play(-1)

def stop_music():
    pygame.mixer.music.stop()

# === Game State ===
theme = None
difficulty = None
snake_speed = 0.1
last_special_food_score = 0
spawn_special_food = False
special_mode = False
special_food_timer = 0
special_mode_timer = 0

# === Replay Menu State ===
replay_menu_stage = 0
replay_options = ["Replay", "Quit"]
replay_turtle = Turtle()
replay_turtle.hideturtle()
replay_turtle.penup()

# === UI Turtles ===
title_turtle = Turtle()
difficulty_turtle = Turtle()
theme_turtle = Turtle()
start_turtle = Turtle()
hint_turtle = Turtle()

# === Menu System State ===
menu_stage = "difficulty"
difficulty_options = ["easy", "medium", "hard"]
theme_options = ["kawaii", "arcade"]
difficulty_index = 0
theme_index = 0
difficulty_locked = False
theme_locked = False

# === Theme Presets ===
themes = {
    "arcade": {
        "bg": "light cyan",
        "snake_color": "#FF69B4",
        "food_color": "deepskyblue",
        "text_color": "deeppink"
    },
    "kawaii": {
        "bg": "mintcream",
        "snake_color": "light pink",
        "food_color": "violet",
        "text_color": "plum"
    }
}

def get_difficulty_speed():
    return {
        "easy": 0.15,
        "medium": 0.1,
        "hard": 0.06
    }[difficulty]

# === Draw Start Menu ===
def draw_start_screen():
    screen.clear()
    screen.bgcolor("black")
    for t in [title_turtle, difficulty_turtle, theme_turtle, start_turtle, hint_turtle]:
        t.clear()
        t.hideturtle()
        t.penup()
        t.speed(0)

    title_turtle.color("white")
    title_turtle.goto(0, 180)
    title_turtle.write("✨ SNAKE.EXE ✨", align="center", font=("Courier", 28, "bold"))

    hint_turtle.color("gray")
    hint_turtle.goto(0, 140)
    hint_turtle.write("Use ⬅️ ➡️ to navigate, ENTER to select", align="center", font=("Courier", 12, "normal"))

    draw_difficulty_options()
    draw_theme_options()
    draw_start_prompt()

def draw_difficulty_options():
    difficulty_turtle.clear()
    y = 100
    spacing = 170
    difficulty_turtle.color("white")
    difficulty_turtle.goto(0, y)
    difficulty_turtle.write("Select Difficulty", align="center", font=("Courier", 16, "underline"))
    y -= 30
    for i, label in enumerate(["1 - Easy", "2 - Medium", "3 - Hard"]):
        x = -spacing + i * spacing
        difficulty_turtle.goto(x, y)
        prefix = "▶ " if i == difficulty_index else ""
        color = "green" if difficulty_locked and difficulty_options[i] == difficulty else "yellow" if i == difficulty_index else "white"
        difficulty_turtle.color(color)
        difficulty_turtle.write(f"{prefix}{label}", align="center", font=("Courier", 14, "bold"))

def draw_theme_options():
    theme_turtle.clear()
    y = 0
    theme_turtle.color("white")
    theme_turtle.goto(0, y)
    theme_turtle.write("Select Theme", align="center", font=("Courier", 16, "underline"))
    y -= 30
    theme_positions = [(-160, "K - Pastel Kawaii"), (160, "A - Arcade 90s")]
    for i, (x, label) in enumerate(theme_positions):
        theme_turtle.goto(x, y)
        prefix = "▶ " if i == theme_index else ""
        color = "magenta" if theme_locked and theme_options[i] == theme else "cyan" if i == theme_index else "white"
        theme_turtle.color(color)
        theme_turtle.write(f"{prefix}{label}", align="center", font=("Courier", 14, "bold"))

def draw_start_prompt():
    start_turtle.clear()
    if difficulty_locked and theme_locked:
        start_turtle.color("cyan")
        start_turtle.goto(0, -140)
        start_turtle.write("Press SPACE to Start", align="center", font=("Courier", 16, "bold"))

# === Menu Navigation ===
def navigate_left():
    global difficulty_index, theme_index
    if menu_stage == "difficulty" and not difficulty_locked:
        difficulty_index = (difficulty_index - 1) % 3
        play_sound("select.wav")
        draw_difficulty_options()
    elif menu_stage == "theme" and not theme_locked:
        theme_index = (theme_index - 1) % 2
        play_sound("select.wav")
        draw_theme_options()

def navigate_right():
    global difficulty_index, theme_index
    if menu_stage == "difficulty" and not difficulty_locked:
        difficulty_index = (difficulty_index + 1) % 3
        play_sound("select.wav")
        draw_difficulty_options()
    elif menu_stage == "theme" and not theme_locked:
        theme_index = (theme_index + 1) % 2
        play_sound("select.wav")
        draw_theme_options()

def confirm_selection():
    global difficulty_locked, theme_locked, difficulty, theme, menu_stage, snake_speed
    if menu_stage == "difficulty" and not difficulty_locked:
        difficulty_locked = True
        difficulty = difficulty_options[difficulty_index]
        snake_speed = get_difficulty_speed()
        play_sound("select.wav")
        draw_difficulty_options()
        menu_stage = "theme"
    elif menu_stage == "theme" and not theme_locked:
        theme_locked = True
        theme = theme_options[theme_index]
        play_sound("select.wav")
        draw_theme_options()
        draw_start_prompt()

def try_start_game():
    if difficulty_locked and theme_locked:
        play_sound("select.wav")
        for t in [title_turtle, difficulty_turtle, theme_turtle, start_turtle, hint_turtle]:
            t.clear()
        play_game()

# === Replay Menu ===
def draw_replay_menu():
    replay_turtle.clear()
    replay_turtle.color(themes[theme]["text_color"])
    y = -60
    positions = [(-100, "Replay"), (100, "Quit")]
    for i, (x, label) in enumerate(positions):
        replay_turtle.goto(x, y)
        text = f"> {label}" if i == replay_menu_stage else label
        font = ("Courier", 16, "bold") if i == replay_menu_stage else ("Courier", 14, "normal")
        replay_turtle.write(text, align="center", font=font)

def replay_left():
    global replay_menu_stage
    replay_menu_stage = (replay_menu_stage - 1) % 2
    play_sound("select.wav")
    draw_replay_menu()

def replay_right():
    global replay_menu_stage
    replay_menu_stage = (replay_menu_stage + 1) % 2
    play_sound("select.wav")
    draw_replay_menu()

def replay_confirm():
    play_sound("select.wav")
    if replay_options[replay_menu_stage] == "Replay":
        reset_state()
        stop_music()
        play_menu_music()
        main()
    else:
        stop_music()
        screen.bye()

# === Game Mechanics ===
def spawn_special_food_if_needed():
    global spawn_special_food, special_food_timer, last_special_food_score
    if scoreboard.score != 0 and scoreboard.score % 5 == 0 and scoreboard.score != last_special_food_score:
        spawn_special_food = True
        special_food_timer = time.time()
        special_food.goto(random.randint(-260, 260), random.randint(-260, 260))
        special_food.showturtle()
        last_special_food_score = scoreboard.score

def handle_special_food():
    global spawn_special_food, special_mode, special_mode_timer
    if spawn_special_food:
        special_food.showturtle() if int(time.time() * 2) % 2 == 0 else special_food.hideturtle()
        if snake.head.distance(special_food) < 15:
            special_food.hideturtle()
            spawn_special_food = False
            special_mode = True
            special_mode_timer = time.time()
            scoreboard.activate_double_points()
            snake.set_glow()
            play_sound("special_mode.mp3")
        elif time.time() - special_food_timer > 5:
            special_food.hideturtle()
            spawn_special_food = False

def handle_special_mode_expiry():
    global special_mode
    if special_mode:
        seconds_left = 10 - int(time.time() - special_mode_timer)
        scoreboard.update_score()
        scoreboard.show_special_mode(seconds_left)
        if seconds_left <= 0:
            special_mode = False
            scoreboard.deactivate_double_points()
            snake.reset_color()
            scoreboard.update_score()

def handle_regular_food():
    global snake_speed, spawn_special_food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        play_sound("food.wav")
        scoreboard.increase_score()
        spawn_special_food_if_needed()
        if spawn_special_food and scoreboard.score % 5 != 0:
            special_food.hideturtle()
            spawn_special_food = False
        if snake_speed > 0.04:
            snake_speed -= 0.005

# === Main Game ===
def play_game():
    global snake, food, scoreboard, special_food
    global last_special_food_score, spawn_special_food, special_mode
    global special_food_timer, special_mode_timer, replay_menu_stage

    stop_music()
    play_game_music()

    # Reset gameplay state
    last_special_food_score = 0
    spawn_special_food = False
    special_mode = False
    special_food_timer = 0
    special_mode_timer = 0
    replay_menu_stage = 0

    screen.clear()
    screen.bgcolor(themes[theme]["bg"])
    screen.tracer(0)

    snake = Snake(themes[theme]["snake_color"])
    food = Food(themes[theme]["food_color"])
    scoreboard = Scoreboard(themes[theme]["text_color"])
    special_food = Food("gold")
    special_food.shape("circle")
    special_food.hideturtle()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(snake_speed)
        snake.move()
        handle_special_food()
        handle_special_mode_expiry()
        handle_regular_food()

        if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
            game_is_on = False
            scoreboard.game_over()
            play_sound("game_over.wav")

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
                play_sound("game_over.wav")

    stop_music()
    draw_replay_menu()
    screen.listen()
    screen.onkey(replay_left, "Left")
    screen.onkey(replay_right, "Right")
    screen.onkey(replay_confirm, "Return")

def reset_state():
    global theme, difficulty, menu_stage
    global difficulty_locked, theme_locked
    global difficulty_index, theme_index
    theme = None
    difficulty = None
    menu_stage = "difficulty"
    difficulty_locked = False
    theme_locked = False
    difficulty_index = 0
    theme_index = 0

def main():
    draw_start_screen()
    screen.listen()
    screen.onkey(navigate_left, "Left")
    screen.onkey(navigate_right, "Right")
    screen.onkey(confirm_selection, "Return")
    screen.onkey(try_start_game, "space")
    play_menu_music()

# === Initialize Screen ===
screen = Screen()
screen.setup(width=600, height=600)
screen.title("SNAKE.EXE")
screen.tracer(0)

main()
screen.mainloop()
