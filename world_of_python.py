import pygame
import random

# Initialize Pygame
pygame.init()

# Game Window
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scary Python Game")

# Fonts
font = pygame.font.Font(None, 36)

# Game State Variables
game_state = "start"  # Start, question1, question2, etc.
player_name = ""
question_text = ""
choices = []
current_choice = ""

# Function to display text on the screen
def draw_text(text, y):
    text_surface = font.render(text, True, (255, 255, 255))  # White text
    text_rect = text_surface.get_rect(center=(WIDTH // 2, y))
    screen.blit(text_surface, text_rect)

# Function to display multi-line text on the screen with wrapping
def draw_multiline_text(text, y, line_height=40):
    words = text.split(' ')
    lines = []
    current_line = ""
    for word in words:
        if font.size(current_line + word)[0] < WIDTH - 40:  # 40 pixels padding
            current_line += word + " "
        else:
            lines.append(current_line)
            current_line = word + " "
    lines.append(current_line)

    for i, line in enumerate(lines):
        draw_text(line.strip(), y + i * line_height)

# Function to handle player input
def handle_input(event):
    global player_name, game_state, current_choice
    if game_state == "start":
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_state = "question1"
                setup_question("Your best friend calls you, but their voice is distorted and faint. They beg you to come to the old abandoned mansion tonight. Do you go? (yes/no)", ["yes", "no"])
            elif event.key == pygame.K_BACKSPACE:
                player_name = player_name[:-1]
            else:
                player_name += event.unicode
    elif game_state.startswith("question"):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                current_choice = "yes"
                handle_choice()
            elif event.key == pygame.K_n:
                current_choice = "no"
                handle_choice()
            elif event.key == pygame.K_f:
                current_choice = "front"
                handle_choice()
            elif event.key == pygame.K_s:
                current_choice = "side"
                handle_choice()
            elif event.key == pygame.K_k:
                current_choice = "kitchen"
                handle_choice()
            elif event.key == pygame.K_l:
                current_choice = "living"
                handle_choice()
            elif event.key == pygame.K_u:
                current_choice = "up"
                handle_choice()
            elif event.key == pygame.K_b:
                current_choice = "basement"
                handle_choice()

def handle_choice():
    global game_state, player_name
    if game_state == "question1":
        if current_choice == "yes":
            game_state = "question2"
            setup_question("Do you enter through the front door or try to find a side entrance? (front/side)", ["front", "side"])
        else:
            setup_question("You decide to stay home, but you can't shake the feeling that you've made a terrible mistake. You hear a scratching noise coming from your closet. Game Over!", [])
    elif game_state == "question2":
        if current_choice == "front":
            game_state = "question3"
            setup_question("You hear a faint whisper coming from the left room. Do you investigate? (yes/no)", ["yes", "no"])
        else:
            game_state = "question4"
            setup_question("You find a broken window and manage to climb inside. You find yourself in the kitchen. Do you explore the kitchen or go to the living room? (kitchen/living)", ["kitchen", "living"])
    elif game_state == "question3":
        if current_choice == "yes":
            game_state = "question5"
            setup_question("You cautiously enter the room. A single flickering candle illuminates a strange symbol on the floor. Suddenly, the candle goes out, and you feel a cold hand grab your arm! A chilling voice whispers 'You shouldn't have come...' Do you run or stay? (run/stay)", ["run", "stay"])
        else:
            game_state = "question6"
            setup_question("You decide to ignore the whisper and continue down the hallway. You see a staircase leading up and a door to the basement. Where do you go? (up/basement)", ["up", "basement"])
    elif game_state == "question4":
        if current_choice == "kitchen":
            game_state = "question7"
            setup_question("You explore the kitchen and find a hidden door behind the pantry. Do you open it? (yes/no)", ["yes", "no"])
        else:
            game_state = "question8"
            setup_question("You go to the living room and find a dusty old book on the table. Do you read it? (yes/no)", ["yes", "no"])
    elif game_state == "question5":
        if current_choice == "run":
            setup_question("You run out of the room and find yourself back in the hallway. Game Over!", [])
        else:
            setup_question("You stay in the room, and the cold hand tightens its grip. Game Over!", [])
    elif game_state == "question6":
        if current_choice == "up":
            game_state = "question9"
            setup_question("You go upstairs and find a locked door. Do you try to pick the lock or look for a key? (pick/key)", ["pick", "key"])
        else:
            game_state = "question10"
            setup_question("You go to the basement and find a strange machine. Do you turn it on? (yes/no)", ["yes", "no"])
    elif game_state == "question7":
        if current_choice == "yes":
            setup_question("You open the hidden door and find a secret passage. Game Over!", [])
        else:
            setup_question("You decide not to open the hidden door and leave the kitchen. Game Over!", [])
    elif game_state == "question8":
        if current_choice == "yes":
            setup_question("You read the dusty old book and discover a hidden message. Game Over!", [])
        else:
            setup_question("You decide not to read the book and leave the living room. Game Over!", [])
    elif game_state == "question9":
        if current_choice == "pick":
            setup_question("You try to pick the lock but fail. Game Over!", [])
        else:
            setup_question("You look for a key and find it under a nearby rug. Game Over!", [])
    elif game_state == "question10":
        if current_choice == "yes":
            setup_question("You turn on the strange machine, and it starts making a loud noise. Game Over!", [])
        else:
            setup_question("You decide not to turn on the machine and leave the basement. Game Over!", [])

# Function to set up a question
def setup_question(text, choices_list):
    global question_text, choices
    question_text = text
    choices = choices_list

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        handle_input(event)

    screen.fill((0, 0, 0))  # Black background

    if game_state == "start":
        draw_text("Welcome to the Scary Game!", 100)
        draw_text("Enter your name: " + player_name, 200)
        draw_text("Press Enter to start", 300)
    elif game_state.startswith("question"):
        draw_multiline_text(question_text, 100)
        y_offset = 200 + (question_text.count('\n') + 1) * 40
        for choice in choices:
            draw_text(f"({choice[0].upper()}) {choice}", y_offset)
            y_offset += 50

    pygame.display.flip()

pygame.quit()