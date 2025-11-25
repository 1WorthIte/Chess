import pygame
import sys

def help():
    pygame.init()

    # Constants
    WIDTH, HEIGHT = 960, 640
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    DARK_GRAY = (169, 169, 169)
    FONT = pygame.font.SysFont(None, 24)

    # Help Content
    help_content = (
        "Objective:\n"
        "The objective of chess is to checkmate your opponent's king (a position where it cannot escape capture.)\n\n"
        "Pieces and Their Moves:\n"
        "King: Moves one square in any direction.\n"
        "Queen: Moves any number of squares in any direction.\n"
        "Rook: Moves any number of squares horizontally or vertically.\n"
        "Bishop: Moves any number of squares diagonally.\n"
        "Knight: Moves in an 'L' shape.\n"
        "Pawn: Moves forward one square or two squares on its first move. Captures diagonally.\n\n"
        "Special Moves:\n"
        "Castling: A move involving the king and either rook, allowing the king and said rook to castle as long as they meet\n"
        "3 conditions: 1. Neither pieces have moved so far in the game 2. The king is not in check 3. The blocks in between\n"
        "the 2 pieces are not under attack)\n"
        "Promotion: When a pawn reaches the end of the board, it can upgrade to either a queen, rook, bishop or knight. \n\n"
        "Check, Checkmate, and Stalemate:\n"
        "Check: A king is in check if it is under threat of capture.\n"
        "Checkmate: The king is in check and there is no legal move to remove the threat.\n"
        "Stalemate: The player to move has no legal move and their king is not in check.\n\n"
        "Draws:\n"
        "Stalemate, Threefold Repetition, Fifty-Move Rule, Insufficient Material."
    )

    # Screen setup
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess Help Menu")

    # Helper functions
    def draw_button(text, x, y, w, h, color, hover_color, action=None):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        button_rect = pygame.Rect(x, y, w, h)
        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, hover_color, button_rect)
            if mouse_click[0] == 1 and action:
                action()
        else:
            pygame.draw.rect(screen, color, button_rect)
        text_surface = FONT.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=button_rect.center)
        screen.blit(text_surface, text_rect)

    def close_help():
        global running_help
        running_help = False

    def draw_help_content(content):
        screen.fill(WHITE)
        lines = content.split('\n')
        y_offset = 50
        for line in lines:
            text_surface = FONT.render(line, True, BLACK)
            screen.blit(text_surface, (50, y_offset))
            y_offset += 22

        draw_button("X", WIDTH - 50, 10, 30, 30, GRAY, DARK_GRAY, close_help)

    # Main loop
    global running_help
    running_help = True
    while running_help:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_help_content(help_content)
        pygame.display.flip()