"""
Name: Mahad Khurram
Date: June 16, 2024
Description: This is a game of chess, that I've poured my heart and soul into. Everything I could possible manage to squeeze in here, I did. For starters, all the pieces move how they're supposed to, it lets the player know
they're in check and adjusts the legal moves accordingly. Checkmate works perfectly, and so does castling (allowing the king and either side rook to castle as long as they meet 3 conditions: 1. Neither pieces have moved so far
in the game 2. The king is not in check 3. The blocks in between the 2 pieces are not under attack). I have slow jazz music playing indefinitely in the background, with separate sounds for either player moving their pieces
and a separate sound for capturing a piece. I've found a way for the pawn to upgrade when it reaches the end of the board, and transforming into either a rook, bishop, knight or even queen. I have a point system built-in, 
letting both players know who's at an advantage in terms of material (how many pieces each person has). Basically, every single feature you could ever want in a game of chess, I've incorporated while ironing out all the bugs
and commenting throughout. This is the 13th version of the game, as I've finally got it to where I want to, with nothing missing.
"""

import pygame
import subprocess
import os
import help

current_dir = os.path.dirname(os.path.abspath(__file__))
script_name = 'game.py'
script_path = os.path.join(current_dir, script_name)

# Initialize Pygame
pygame.init()
pygame.mixer.init()
jazz = pygame.mixer.Sound("jazz.mp3")
jazz.set_volume(0.3)
jazz.play(-1)

# Set up the display
window = pygame.display.set_mode((960, 640))

# Load background image
background = pygame.image.load("menu.png")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
HOVER_COLOR = (200, 200, 200)  # Color for button when hovered over

# Define fonts
font = pygame.font.Font(None, 74)
button_font = pygame.font.Font(None, 50)

# Define text
text = font.render('Chess', True, WHITE)

# Define buttons
button1 = pygame.Rect(50, 100, 200, 50)
button2 = pygame.Rect(50, 200, 200, 50)

# Main loop
while True:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(event.pos):
                # Run the game script
                jazz.stop()
                pygame.quit()
                subprocess.run(['python3', script_path], shell=False)
            if button2.collidepoint(event.pos):
                help.help()

    # Fill the window with the background image
    window.blit(background, (0, 0))

    # Draw text
    window.blit(text, (400, 50))

    # Draw buttons with hover effect
    if button1.collidepoint(mouse_pos):
        pygame.draw.rect(window, HOVER_COLOR, button1)
    else:
        pygame.draw.rect(window, GRAY, button1)

    if button2.collidepoint(mouse_pos):
        pygame.draw.rect(window, HOVER_COLOR, button2)
    else:
        pygame.draw.rect(window, GRAY, button2)

    # Draw button text
    button1_text = button_font.render('Play', True, BLACK)
    button2_text = button_font.render('Rules', True, BLACK)

    window.blit(button1_text, (button1.x + 10, button1.y + 10))
    window.blit(button2_text, (button2.x + 10, button2.y + 10))

    # Update the display
    pygame.display.flip()