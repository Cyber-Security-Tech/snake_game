
# ✨ SNAKE.EXE ✨

A retro-styled, fully polished Snake game built using Python and the Turtle graphics module — enhanced with sound effects, theme customization, animated menus, difficulty selection, special modes, and persistent high score tracking.

## 🎮 Features

- **Animated Start Menu**  
  Navigate using arrow keys and confirm selections with ENTER — choose from:
  - Difficulty: Easy, Medium, Hard
  - Theme: Pastel Kawaii 🌸 or Arcade 90s 🎮

- **Sound Effects + Music**  
  - Menu and game themes with looping background music  
  - Distinct sounds for selection, special mode, food, game over, and high score!

- **Smooth Gameplay Mechanics**
  - Classic snake behavior: movement, growth, wall and tail collision
  - Gradual speed increase for added challenge
  - Polished game loop and controls (arrow keys to move)

- **Special Mode Power-Up**  
  Every 5 points, a flashing gold food appears. If eaten quickly:
  - Snake glows gold ✨
  - Double points for 10 seconds
  - Special mode countdown shown on screen

- **High Score System**
  - Tracks and saves your highest score in a text file  
  - Celebrates with a flashing "NEW HIGH SCORE!" animation and sound

- **Replay Menu with Arrow Navigation**
  - After Game Over, use ⬅️ ➡️ to select:
    - **Replay**
    - **Quit**

## 🐍 Technologies Used

- Python 3
- Turtle graphics module
- `playsound` for sound effects
- `pygame.mixer` for looping background music
- Object-Oriented Programming (OOP) design

## 🧠 What I Learned

This project was a deep dive into:
- Real-time game logic
- OOP best practices and modular design
- Event-driven programming with `tkinter`-style bindings
- Audio integration in Python using both `playsound` and `pygame.mixer`
- UI/UX design within the limitations of Turtle graphics
- Debugging and polishing edge cases for a smooth user experience

## 📂 Project Structure

```
snake_game/
├── main.py
├── snake.py
├── food.py
├── scoreboard.py
├── sounds/
│   ├── menu_theme.mp3
│   ├── game_theme.wav
│   ├── select.wav
│   ├── food.wav
│   ├── special_mode.mp3
│   ├── game_over.wav
│   └── new_high_score.wav
├── high_score.txt
```

## 🚀 How to Run

1. Clone this repo:
   ```
   git clone https://github.com/yourusername/snake_game.git
   ```

2. Install requirements:
   ```
   pip install playsound pygame
   ```

3. Run the game:
   ```
   python main.py
   ```
