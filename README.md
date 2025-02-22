# Scary Python Game

This is a simple text-based horror game created with Python and Pygame. The game presents the player with a series of choices that lead them through a spooky abandoned mansion.

## Prerequisites

* Python 3.x
* Pygame library (`pip install pygame`)

## How to Run

1.  **Install Pygame:**
    ```bash
    pip install pygame
    ```
2.  **Save the code:** Save the provided Python code as a `.py` file (e.g., `scary_game.py`).
3.  **Run the game:**
    ```bash
    python scary_game.py
    ```

## Game Instructions

* The game starts with a welcome screen where you enter your name and press Enter to begin.
* You'll be presented with a series of text-based choices.
* To make a choice, press the corresponding key (e.g., 'y' for yes, 'n' for no, 'f' for front, 's' for side, etc.).
* The game's outcome depends on the choices you make.
* Most choices lead to a "Game Over" screen.

## Game Features

* Text-based adventure with choices and consequences.
* Simple Pygame interface for displaying text.
* Multi-line text wrapping for longer questions.
* Multiple game paths and endings.
* Uses random elements to add to the spooky atmosphere.

## Code Explanation

* **Pygame Initialization:** The code initializes Pygame and creates a game window.
* **Fonts:** The code sets a font for displaying text.
* **Game State:** The `game_state` variable tracks the current state of the game.
* **Input Handling:** The `handle_input()` function processes keyboard input.
* **Choice Handling:** The `handle_choice()` function determines the next game state based on the player's choices.
* **Text Display:** The `draw_text()` and `draw_multiline_text()` functions render text onto the screen.
* **Game Loop:** The main game loop handles events, updates the game state, and draws the screen.
* **Setup Questions:** The `setup_question()` function sets the questions and the available choices.

## Future Improvements

* Add images and sound effects to enhance the atmosphere.
* Implement a more complex game logic with puzzles and items.
* Create a more user-friendly interface with buttons and menus.
* Add more varied endings, and potentially a way to win the game.
* Refactor the code into classes for better organization.
* Add error handling.
