#!/usr/bin/env python3

import pygame

pygame.init()

# Window size
WIDTH, HEIGHT = 960, 640
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Chess")

pygame.mixer.init()
jazz = pygame.mixer.Sound("jazz.mp3")
move1 = pygame.mixer.Sound('piece_move_1.mp3')
move2 = pygame.mixer.Sound('piece_move_2.mp3')
jazz.set_volume(0.3)
jazz.play(-1)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT = (255, 255, 255)
LIGHT_GRAY = (230, 230, 230)
WHITE_SCORE_COLOR = (255, 100, 100)
BLACK_SCORE_COLOR = (100, 100, 255)

# Load images
ApawnB = pygame.image.load("pawnBlack.png")
BpawnB = pygame.image.load("pawnBlack.png")
CpawnB = pygame.image.load("pawnBlack.png")
DpawnB = pygame.image.load("pawnBlack.png")
EpawnB = pygame.image.load("pawnBlack.png")
FpawnB = pygame.image.load("pawnBlack.png")
GpawnB = pygame.image.load("pawnBlack.png")
HpawnB = pygame.image.load("pawnBlack.png")
LrookB = pygame.image.load("rookBlack.png")
RrookB = pygame.image.load("rookBlack.png")
LknightB = pygame.image.load("knightBlack.png")
RknightB = pygame.image.load("knightBlack.png")
LbishopB = pygame.image.load("bishopBlack.png")
RbishopB = pygame.image.load("bishopBlack.png")
kingB = pygame.image.load("kingBlack.png")
queenB = pygame.image.load("queenBlack.png")

ApawnW = pygame.image.load("pawnWhite.png")
BpawnW = pygame.image.load("pawnWhite.png")
CpawnW = pygame.image.load("pawnWhite.png")
DpawnW = pygame.image.load("pawnWhite.png")
EpawnW = pygame.image.load("pawnWhite.png")
FpawnW = pygame.image.load("pawnWhite.png")
GpawnW = pygame.image.load("pawnWhite.png")
HpawnW = pygame.image.load("pawnWhite.png")
LrookW = pygame.image.load("rookWhite.png")
RrookW = pygame.image.load("rookWhite.png")
LknightW = pygame.image.load("knightWhite.png")
RknightW = pygame.image.load("knightWhite.png")
LbishopW = pygame.image.load("bishopWhite.png")
RbishopW = pygame.image.load("bishopWhite.png")
kingW = pygame.image.load("kingWhite.png")
queenW = pygame.image.load("queenWhite.png")

score_difference = 0

board = pygame.image.load("board.jpg")
promotion_needed = False

# Font
font = pygame.font.SysFont(None, 24)

# Positions
spots = {
"a9": [700, 0, 0], "b9": [700, 0, 0], "c9": [700, 0, 0], "d9": [700, 0, 0], "e9": [700, 0, 0], "f9": [700, 0, 0], "g9": [700, 0, 0], "h9": [700, 0, 0],
      "a8": [0, 0, LrookB], "b8": [80, 0, LknightB], "c8": [160, 0, LbishopB], "d8": [240, 0, queenB], "e8": [320, 0, kingB], "f8": [400, 0, RbishopB], "g8": [480, 0, RknightB], "h8": [560, 0, RrookB],
      "a7": [0, 80, ApawnB], "b7": [80, 80, BpawnB], "c7": [160, 80, CpawnB], "d7": [240, 80, DpawnB], "e7": [320, 80, EpawnB], "f7": [400, 80, FpawnB], "g7": [480, 80, GpawnB], "h7": [560, 80, HpawnB],
      "a6": [0, 160, 0], "b6": [80, 160, 0], "c6": [160, 160, 0], "d6": [240, 160, 0], "e6": [320, 160, 0], "f6": [400, 160, 0], "g6": [480, 160, 0], "h6": [560, 160, 0],
      "a5": [0, 240, 0], "b5": [80, 240, 0], "c5": [160, 240, 0], "d5": [240, 240, 0], "e5": [320, 240, 0], "f5": [400, 240, 0], "g5": [480, 240, 0], "h5": [560, 240, 0],
      "a4": [0, 320, 0], "b4": [80, 320, 0], "c4": [160, 320, 0], "d4": [240, 320, 0], "e4": [320, 320, 0], "f4": [400, 320, 0], "g4": [480, 320, 0], "h4": [560, 320, 0],
      "a3": [0, 400, 0], "b3": [80, 400, 0], "c3": [160, 400, 0], "d3": [240, 400, 0], "e3": [320, 400, 0], "f3": [400, 400, 0], "g3": [480, 400, 0], "h3": [560, 400, 0],
      "a2": [0, 480, ApawnW], "b2": [80, 480, BpawnW], "c2": [160, 480, CpawnW], "d2": [240, 480, DpawnW], "e2": [320, 480, EpawnW], "f2": [400, 480, FpawnW], "g2": [480, 480, GpawnW], "h2": [560, 480, HpawnW],
      "a1": [0, 560, LrookW], "b1": [80, 560, LknightW], "c1": [160, 560, LbishopW], "d1": [240, 560, queenW], "e1": [320, 560, kingW], "f1": [400, 560, RbishopW], "g1": [480, 560, RknightW], "h1": [560, 560, RrookW],
      "a0": [700, 0, 0], "b0": [700, 0, 0], "c0": [700, 0, 0], "d0": [700, 0, 0], "e0": [700, 0, 0], "f0": [700, 0, 0], "g0": [700, 0, 0], "h0": [700, 0, 0],
}

# Constants for the castling moves
CASTLE_KING_SIDE_BLACK = 'h8'
CASTLE_QUEEN_SIDE_BLACK = 'a8'
CASTLE_KING_SIDE_WHITE = 'h1'
CASTLE_QUEEN_SIDE_WHITE = 'a1'

# Define variables to track whether castling is still possible
white_king_moved = False
white_king_rook_moved = False
white_queen_rook_moved = False

black_king_moved = False
black_king_rook_moved = False
black_queen_rook_moved = False

blocks = {}
for key, (x, y, piece) in spots.items():
      blocks[key] = pygame.Rect(x, y, 80, 80)

letters = {chr(97 + i): font.render(chr(97 + i), True, BLACK) for i in range(8)}
numbers = {i + 1: font.render(str(i + 1), True, BLACK) for i in range(8)}

selected_piece = None
selected_pos = None
highlighted_moves = []

last_double_step_pawn = None

turn = "white"

piece_values = {
'pawn': 1,
'knight': 3,
'bishop': 3,
'rook': 5,
'ueen': 9,
}

captured_white = []
captured_black = []

def get_var_name(var):
      for name, value in globals().items():
            if value is var:
                  return name

def capture_piece(captured_piece, player):
      if player == 'white':
            captured_black.append(captured_piece)
      else:
            captured_white.append(captured_piece)

def calculate_score(captured_pieces):
      score = 0
      for piece in captured_pieces:
            score += piece_values[get_var_name(piece)[1:-1]]
      return score

def is_in_check(king_pos, spots, color):
      for pos, (_, _, piece) in spots.items():
            if piece != 0 and ((color == "white" and piece in [ApawnB, BpawnB, CpawnB, DpawnB, EpawnB, FpawnB, GpawnB, HpawnB, LrookB, RrookB, LknightB, RknightB, LbishopB, RbishopB, queenB, kingB]) or (color == "black" and piece in [ApawnW, BpawnW, CpawnW, DpawnW, EpawnW, FpawnW, GpawnW, HpawnW, LrookW, RrookW, LknightW, RknightW, LbishopW, RbishopW, queenW, kingW])):
                  possible_moves = get_possible_moves(piece, pos)
                  if king_pos in possible_moves:
                        return True
      return False

def is_checkmate(king_pos, spots, color):
      if not is_in_check(king_pos, spots, color):
            return False
      for pos, (_, _, piece) in spots.items():
            if (color == "white" and piece in [ApawnW, BpawnW, CpawnW, DpawnW, EpawnW, FpawnW, GpawnW, HpawnW, LrookW, RrookW, LknightW, RknightW, LbishopW, RbishopW, queenW, kingW]) or (color == "black" and piece in [ApawnB, BpawnB, CpawnB, DpawnB, EpawnB, FpawnB, GpawnB, HpawnB, LrookB, RrookB, LknightB, RknightB, LbishopB, RbishopB, queenB, kingB]):
                  original_pos = pos
                  possible_moves = get_possible_moves(piece, pos)
                  for move in possible_moves:
                        original_piece = spots[move][2]
                        spots[move][2] = piece
                        spots[original_pos][2] = 0
                        if not is_in_check(king_pos, spots, color):
                              spots[move][2] = original_piece
                              spots[original_pos][2] = piece
                              return False
                        spots[move][2] = original_piece
                        spots[original_pos][2] = piece
      return True

def execute_move(start, end):
      global last_double_step_pawn
      piece = spots[start][2]

      if piece in [ApawnW, BpawnW, CpawnW, DpawnW, EpawnW, FpawnW, GpawnW, HpawnW]:
            if end[1] == '8':  # Promotion
                  piece = promotion_popup(window, "white")
                  piece = {"Queen": queenW, "Rook": LrookW, "Bishop": LbishopW, "Knight": LknightW}[piece]
      elif piece in [ApawnB, BpawnB, CpawnB, DpawnB, EpawnB, FpawnB, GpawnB, HpawnB]:
            if end[1] == '1':  # Promotion
                  piece = promotion_popup(window, "black")
                  piece = {"Queen": queenB, "Rook": LrookB, "Bishop": LbishopB, "Knight": LknightB}[piece]

      spots[end][2] = piece
      spots[start][2] = 0


def promotion_popup(screen, color):
      # Set up the promotion window dimensions
      width, height = 200, 100
      x, y = (screen.get_width() - width) // 2, (screen.get_height() - height) // 2

      # Create a new surface for the pop-up
      popup = pygame.Surface((width, height))
      popup.fill((255, 255, 255))
      pygame.draw.rect(popup, (0, 0, 0), popup.get_rect(), 2)

      # Define the buttons for promotion
      font = pygame.font.Font(None, 36)
      buttons = []
      pieces = ["Queen", "Rook", "Bishop", "Knight"]
      for i, piece in enumerate(pieces):
            button = font.render(piece, True, (0, 0, 0))
            button_rect = button.get_rect(center=(width // 2, 20 + i * 20))
            buttons.append((button, button_rect, piece))

      # Event loop for the promotion pop-up
      running = True
      while running:
            screen.blit(popup, (x, y))
            for button, rect, piece in buttons:
                  screen.blit(button, (x + rect.x, y + rect.y))

            pygame.display.flip()

            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                  elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos
                        for button, rect, piece in buttons:
                              if rect.collidepoint(mouse_pos[0] - x, mouse_pos[1] - y):
                                    return piece  # Return the selected piece

def get_possible_moves(piece, pos):
      x, y = ord(pos[0]) - 97, 8 - int(pos[1])
      moves = []
      global promotion_needed

      moves.clear()

      if piece in [ApawnW, BpawnW, CpawnW, DpawnW, EpawnW, FpawnW, GpawnW, HpawnW]:
            # White pawn logic
            if y >= 0:  # Ensure we're not at the last rank
                  # Check single square move
                  if spots[f"{chr(x + 97)}{8 - (y - 1)}"][2] == 0:
                        if y == 0:
                              # Promotion
                              promotion_needed = True
                        moves.append(f"{chr(x + 97)}{8 - (y - 1)}")
                  # Check double square move for first move
                  if y == 6 and spots[f"{chr(x + 97)}{8 - (y - 1)}"][2] == 0 and spots[f"{chr(x + 97)}{8 - (y - 2)}"][2] == 0:
                        moves.append(f"{chr(x + 97)}{8 - (y - 2)}")
                  # Check captures
                  if x > 0 and spots[f"{chr(x + 96)}{8 - (y - 1)}"][2] in [ApawnB, BpawnB, CpawnB, DpawnB, EpawnB, FpawnB, GpawnB, HpawnB, LrookB, RrookB, LknightB, RknightB, LbishopB, RbishopB, queenB, kingB]:
                        if y == 0:
                              # Promotion on capture
                              promotion_needed = True
                        moves.append(f"{chr(x + 96)}{8 - (y - 1)}")
                  if x < 7 and spots[f"{chr(x + 98)}{8 - (y - 1)}"][2] in [ApawnB, BpawnB, CpawnB, DpawnB, EpawnB, FpawnB, GpawnB, HpawnB, LrookB, RrookB, LknightB, RknightB, LbishopB, RbishopB, queenB, kingB]:
                        if y == 0:
                              # Promotion on capture
                              promotion_needed = True
                        moves.append(f"{chr(x + 98)}{8 - (y - 1)}")

      elif piece in [ApawnB, BpawnB, CpawnB, DpawnB, EpawnB, FpawnB, GpawnB, HpawnB]:
            # Black pawn logic
            if y <= 7:  # Ensure we're not at the last rank
                  # Check single square move
                  if spots[f"{chr(x + 97)}{8 - (y + 1)}"][2] == 0:
                        if y == 7:
                              # Promotion
                              promotion_needed = True
                        moves.append(f"{chr(x + 97)}{8 - (y + 1)}")
                  # Check double square move for first move
                  if y == 1 and spots[f"{chr(x + 97)}{8 - (y + 1)}"][2] == 0 and spots[f"{chr(x + 97)}{8 - (y + 2)}"][2] == 0:
                        moves.append(f"{chr(x + 97)}{8 - (y + 2)}")
                  # Check captures
                  if x > 0 and spots[f"{chr(x + 96)}{8 - (y + 1)}"][2] in [ApawnW, BpawnW, CpawnW, DpawnW, EpawnW, FpawnW, GpawnW, HpawnW, LrookW, RrookW, LknightW, RknightW, LbishopW, RbishopW, queenW, kingW]:
                        if y == 7:
                              # Promotion on capture
                              promotion_needed = True
                        moves.append(f"{chr(x + 96)}{8 - (y + 1)}")
                  if x < 7 and spots[f"{chr(x + 98)}{8 - (y + 1)}"][2] in [ApawnW, BpawnW, CpawnW, DpawnW, EpawnW, FpawnW, GpawnW, HpawnW, LrookW, RrookW, LknightW, RknightW, LbishopW, RbishopW, queenW, kingW]:
                        if y == 7:
                              # Promotion on capture
                              promotion_needed = True
                        moves.append(f"{chr(x + 98)}{8 - (y + 1)}")

      elif piece in [LrookW, RrookW, LrookB, RrookB]:
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                  nx, ny = x + dx, y + dy
                  while 0 <= nx < 8 and 0 <= ny < 8:
                        if spots[f"{chr(nx + 97)}{8 - ny}"][2] == 0:
                              moves.append(f"{chr(nx + 97)}{8 - ny}")
                        elif (piece in [LrookW, RrookW] and spots[f"{chr(nx + 97)}{8 - ny}"][2] in [ApawnB, BpawnB, CpawnB, DpawnB, EpawnB, FpawnB, GpawnB, HpawnB, LrookB, RrookB, LknightB, RknightB, LbishopB, RbishopB, queenB, kingB]) or (piece in [LrookB, RrookB] and spots[f"{chr(nx + 97)}{8 - ny}"][2] in [ApawnW, BpawnW, CpawnW, DpawnW, EpawnW, FpawnW, GpawnW, HpawnW, LrookW, RrookW, LknightW, RknightW, LbishopW, RbishopW, queenW, kingW]):
                              moves.append(f"{chr(nx + 97)}{8 - ny}")
                              break
                        else:
                              break
                        nx += dx
                        ny += dy

      elif piece in [LknightW, RknightW, LknightB, RknightB]:
            knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
            for dx, dy in knight_moves:
                  nx, ny = x + dx, y + dy
                  if 0 <= nx < 8 and 0 <= ny < 8:
                        if spots[f"{chr(nx + 97)}{8 - ny}"][2] == 0 or ((piece in [LknightW, RknightW] and spots[f"{chr(nx + 97)}{8 - ny}"][2] in [ApawnB, BpawnB, CpawnB, DpawnB, EpawnB, FpawnB, GpawnB, HpawnB, LrookB, RrookB, LknightB, RknightB, LbishopB, RbishopB, queenB, kingB]) or (piece in [LknightB, RknightB] and spots[f"{chr(nx + 97)}{8 - ny}"][2] in [ApawnW, BpawnW, CpawnW, DpawnW, EpawnW, FpawnW, GpawnW, HpawnW, LrookW, RrookW, LknightW, RknightW, LbishopW, RbishopW, queenW, kingW])):
                              moves.append(f"{chr(nx + 97)}{8 - ny}")

      elif piece in [LbishopW, RbishopW, LbishopB, RbishopB]:
            directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
            for dx, dy in directions:
                  nx, ny = x + dx, y + dy
                  while 0 <= nx < 8 and 0 <= ny < 8:
                        if spots[f"{chr(nx + 97)}{8 - ny}"][2] == 0:
                              moves.append(f"{chr(nx + 97)}{8 - ny}")
                        elif (piece in [LbishopW, RbishopW] and spots[f"{chr(nx + 97)}{8 - ny}"][2] in [ApawnB, BpawnB, CpawnB, DpawnB, EpawnB, FpawnB, GpawnB, HpawnB, LrookB, RrookB, LknightB, RknightB, LbishopB, RbishopB, queenB, kingB]) or (piece in [LbishopB, RbishopB] and spots[f"{chr(nx + 97)}{8 - ny}"][2] in [ApawnW, BpawnW, CpawnW, DpawnW, EpawnW, FpawnW, GpawnW, HpawnW, LrookW, RrookW, LknightW, RknightW, LbishopW, RbishopW, queenW, kingW]):
                              moves.append(f"{chr(nx + 97)}{8 - ny}")
                              break
                        else:
                              break
                        nx += dx
                        ny += dy

      elif piece in [queenW, queenB]:
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
            for dx, dy in directions:
                  nx, ny = x + dx, y + dy
                  while 0 <= nx < 8 and 0 <= ny < 8:
                        if spots[f"{chr(nx + 97)}{8 - ny}"][2] == 0:
                              moves.append(f"{chr(nx + 97)}{8 - ny}")
                        elif (piece == queenW and spots[f"{chr(nx + 97)}{8 - ny}"][2] in [ApawnB, BpawnB, CpawnB, DpawnB, EpawnB, FpawnB, GpawnB, HpawnB, LrookB, RrookB, LknightB, RknightB, LbishopB, RbishopB, queenB, kingB]) or (piece == queenB and spots[f"{chr(nx + 97)}{8 - ny}"][2] in [ApawnW, BpawnW, CpawnW, DpawnW, EpawnW, FpawnW, GpawnW, HpawnW, LrookW, RrookW, LknightW, RknightW, LbishopW, RbishopW, queenW, kingW]):
                              moves.append(f"{chr(nx + 97)}{8 - ny}")
                              break
                        else:
                              break
                        nx += dx
                        ny += dy

      elif piece == kingW:
            # Normal king moves
            for dx in [-1, 0, 1]:
                  for dy in [-1, 0, 1]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < 8 and 0 <= ny < 8:
                              if spots[f"{chr(nx + 97)}{8 - ny}"][2] == 0 or spots[f"{chr(nx + 97)}{8 - ny}"][2] in [ApawnB, BpawnB, CpawnB, DpawnB, EpawnB, FpawnB, GpawnB, HpawnB, LrookB, RrookB, LknightB, RknightB, LbishopB, RbishopB, queenB, kingB]:
                                    moves.append(f"{chr(nx + 97)}{8 - ny}")
            # Castling moves for white king
            if can_castle('white', 'king-side'):
                  if not white_king_moved and not white_king_rook_moved:
                        moves.append(CASTLE_KING_SIDE_WHITE)  # This should be the destination square for king-side castle
            if can_castle('white', 'queen-side'):
                  if not white_king_moved and not white_queen_rook_moved:
                        moves.append(CASTLE_QUEEN_SIDE_WHITE)  # This should be the destination square for queen-side castle

      elif piece == kingB:
            # Normal king moves
            for dx in [-1, 0, 1]:
                  for dy in [-1, 0, 1]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < 8 and 0 <= ny < 8:
                              if spots[f"{chr(nx + 97)}{8 - ny}"][2] == 0 or spots[f"{chr(nx + 97)}{8 - ny}"][2] in [ApawnW, BpawnW, CpawnW, DpawnW, EpawnW, FpawnW, GpawnW, HpawnW, LrookW, RrookW, LknightW, RknightW, LbishopW, RbishopW, queenW, kingW]:
                                    moves.append(f"{chr(nx + 97)}{8 - ny}")
            # Castling moves for black king
            if can_castle('black', 'king-side'):
                  if not black_king_moved and not black_king_rook_moved:
                        moves.append(CASTLE_KING_SIDE_BLACK)  # This should be the destination square for king-side castle
            if can_castle('black', 'queen-side'):
                  if not black_king_moved and not black_queen_rook_moved:
                        moves.append(CASTLE_QUEEN_SIDE_BLACK)  # This should be the destination square for queen-side castle

      return moves


def can_castle(color, side):
      if color == 'white':
            if side == 'king-side':
                  if spots['e1'][2] == kingW and spots['h1'][2] == RrookW and \
                  spots['f1'][2] == 0 and spots['g1'][2] == 0 and \
                  not is_in_check('e1', spots, 'white') and \
                  not is_in_check('f1', spots, 'white') and \
                  not is_in_check('g1', spots, 'white'):
                        return True
            elif side == 'queen-side':
                  if spots['e1'][2] == kingW and spots['a1'][2] == LrookW and \
                  spots['b1'][2] == 0 and spots['c1'][2] == 0 and spots['d1'][2] == 0 and \
                  not is_in_check('e1', spots, 'white') and \
                  not is_in_check('c1', spots, 'white') and \
                  not is_in_check('d1', spots, 'white'):
                        return True
      elif color == 'black':
            if side == 'king-side':
                  if spots['e8'][2] == kingB and spots['h8'][2] == RrookB and \
                  spots['f8'][2] == 0 and spots['g8'][2] == 0 and \
                  not is_in_check('e8', spots, 'black') and \
                  not is_in_check('f8', spots, 'black') and \
                  not is_in_check('g8', spots, 'black'):
                        return True
            elif side == 'queen-side':
                  if spots['e8'][2] == kingB and spots['a8'][2] == LrookB and \
                  spots['b8'][2] == 0 and spots['c8'][2] == 0 and spots['d8'][2] == 0 and \
                  not is_in_check('e8', spots, 'black') and \
                  not is_in_check('c8', spots, 'black') and \
                  not is_in_check('d8', spots, 'black'):
                        return True
      return False

def has_legal_moves(spots, turn):
      for pos, data in spots.items():
            piece = data[2]
            if (turn == "white" and piece in [ApawnW, BpawnW, CpawnW, DpawnW, EpawnW, FpawnW, GpawnW, HpawnW, LrookW, RrookW, LknightW, RknightW, LbishopW, RbishopW, queenW, kingW]) or \
            (turn == "black" and piece in [ApawnB, BpawnB, CpawnB, DpawnB, EpawnB, FpawnB, GpawnB, HpawnB, LrookB, RrookB, LknightB, RknightB, LbishopB, RbishopB, queenB, kingB]):
                  moves = get_possible_moves(piece, pos)
                  for move in moves:
                        original_piece_at_dest = spots[move][2]
                        spots[move][2] = piece
                        spots[pos][2] = 0

                        if turn == "white":
                              king_pos_w = [k for k, v in spots.items() if v[2] == kingW][0]
                              if not is_in_check(king_pos_w, spots, "white"):
                                    spots[pos][2] = piece
                                    spots[move][2] = original_piece_at_dest
                                    return True
                        else:
                              king_pos_b = [k for k, v in spots.items() if v[2] == kingB][0]
                              if not is_in_check(king_pos_b, spots, "black"):
                                    spots[pos][2] = piece
                                    spots[move][2] = original_piece_at_dest
                                    return True

                        spots[pos][2] = piece
                        spots[move][2] = original_piece_at_dest

      return False

running = True
while running:
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                  x, y = event.pos
                  for key, rect in blocks.items():
                        if rect.collidepoint(x, y):
                              if selected_piece is None:
                                    if spots[key][2] != 0 and (
                                          (turn == "white" and spots[key][2] in [ApawnW, BpawnW, CpawnW, DpawnW, EpawnW, FpawnW, GpawnW, HpawnW, LrookW, RrookW, LknightW, RknightW, LbishopW, RbishopW, queenW, kingW]) or
                                          (turn == "black" and spots[key][2] in [ApawnB, BpawnB, CpawnB, DpawnB, EpawnB, FpawnB, GpawnB, HpawnB, LrookB, RrookB, LknightB, RknightB, LbishopB, RbishopB, queenB, kingB])
                                    ):
                                          selected_piece = spots[key][2]
                                          selected_pos = key

                                          # Get possible moves and filter out moves that put the player in check
                                          possible_moves = get_possible_moves(selected_piece, selected_pos)
                                          highlighted_moves = []
                                          for move in possible_moves:
                                                original_piece_at_dest = spots[move][2]
                                                spots[move][2] = selected_piece
                                                spots[selected_pos][2] = 0

                                                if turn == "white":
                                                      king_pos_w = [k for k, v in spots.items() if v[2] == kingW][0]
                                                      if not is_in_check(king_pos_w, spots, "white"):
                                                            highlighted_moves.append(move)
                                                else:
                                                      king_pos_b = [k for k, v in spots.items() if v[2] == kingB][0]
                                                      if not is_in_check(king_pos_b, spots, "black"):
                                                            highlighted_moves.append(move)

                                                # Revert the move
                                                spots[selected_pos][2] = selected_piece
                                                spots[move][2] = original_piece_at_dest
                              else:
                                    # Updating movement history when a piece moves
                                    if selected_piece == kingW:
                                          white_king_moved = True
                                    if selected_piece == RrookW:
                                          white_king_rook_moved = True
                                    if selected_piece == LrookW:
                                          white_queen_rook_moved = True
                                    if selected_piece == kingB:
                                          black_king_moved = True
                                    if selected_piece == RrookB:
                                          black_king_rook_moved = True
                                    if selected_piece == LrookB:
                                          black_queen_rook_moved = True
                                    if key in highlighted_moves:
                                          if key == CASTLE_KING_SIDE_WHITE and can_castle("white", "king-side"):
                                                spots['g1'][2] = kingW
                                                spots['f1'][2] = RrookW
                                                spots['e1'][2] = 0
                                                spots['h1'][2] = 0
                                                white_king_moved = True
                                                white_king_rook_moved = True
                                          elif key == CASTLE_QUEEN_SIDE_WHITE and can_castle("white", "queen-side"):
                                                spots['c1'][2] = kingW
                                                spots['d1'][2] = LrookW
                                                spots['e1'][2] = 0
                                                spots['a1'][2] = 0
                                                white_king_moved = True
                                                white_queen_rook_moved = True
                                          elif key == CASTLE_KING_SIDE_BLACK and can_castle("black", "king-side"):
                                                spots['g8'][2] = kingB
                                                spots['f8'][2] = RrookB
                                                spots['e8'][2] = 0
                                                spots['h8'][2] = 0
                                                black_king_moved = True
                                                black_king_rook_moved = True
                                          elif key == CASTLE_QUEEN_SIDE_BLACK and can_castle("black", "queen-side"):
                                                spots['c8'][2] = kingB
                                                spots['d8'][2] = LrookB
                                                spots['e8'][2] = 0
                                                spots['a8'][2] = 0
                                                black_king_moved = True
                                                black_queen_rook_moved = True
                                          else:      
                                                # Temporarily make the move
                                                original_piece_at_dest = spots[key][2]
                                                if original_piece_at_dest != 0:
                                                      capture_piece(original_piece_at_dest, turn)
                                                execute_move(selected_pos, key)

                                          # Check if this move puts the player in check
                                          if turn == "white":
                                                king_pos_w = [k for k, v in spots.items() if v[2] == kingW][0]
                                                if is_in_check(king_pos_w, spots, "white"):
                                                      # Revert the move
                                                      spots[selected_pos][2] = selected_piece
                                                      spots[key][2] = original_piece_at_dest
                                                      continue
                                          else:
                                                king_pos_b = [k for k, v in spots.items() if v[2] == kingB][0]
                                                if is_in_check(king_pos_b, spots, "black"):
                                                      # Revert the move
                                                      spots[selected_pos][2] = selected_piece
                                                      spots[key][2] = original_piece_at_dest
                                                      continue

                                          # Confirm the move
                                          if turn == "white":
                                                pygame.mixer.find_channel().play(move1)
                                                turn = "black"
                                                if not has_legal_moves(spots, "black"):
                                                      king_pos_b = [k for k, v in spots.items() if v[2] == kingB][0]
                                                      if is_in_check(king_pos_b, spots, "black"):
                                                            message = font.render("Checkmate! White wins!", True, BLACK)
                                                      else:
                                                            message = font.render("Stalemate! It's a draw!", True, BLACK)
                                                      window.blit(message, (660, HEIGHT // 2 - message.get_height() // 2))
                                                      pygame.display.update()
                                                      pygame.time.wait(3000)
                                                      running = False
                                                elif is_in_check(king_pos_w, spots, "white"):
                                                      message = font.render("Check!", True, BLACK)
                                                      window.blit(message, (660, HEIGHT // 2 - message.get_height() // 2))
                                                      pygame.display.update()
                                                      pygame.time.wait(1000)
                                          else:
                                                pygame.mixer.find_channel().play(move2)
                                                turn = "white"
                                                if not has_legal_moves(spots, "white"):
                                                      king_pos_w = [k for k, v in spots.items() if v[2] == kingW][0]
                                                      if is_in_check(king_pos_w, spots, "white"):
                                                            message = font.render("Checkmate! Black wins!", True, BLACK)
                                                      else:
                                                            message = font.render("Stalemate! It's a draw!", True, BLACK)
                                                      window.blit(message, (660, HEIGHT // 2 - message.get_height() // 2))
                                                      pygame.display.update()
                                                      pygame.time.wait(3000)
                                                      running = False
                                                elif is_in_check(king_pos_b, spots, "black"):
                                                      message = font.render("Check!", True, BLACK)
                                                      window.blit(message, (660, HEIGHT // 2 - message.get_height() // 2))
                                                      pygame.display.update()
                                                      pygame.time.wait(1000)
                                                      
                                          selected_piece = None
                                          selected_pos = None
                                          highlighted_moves = []
                                    else:
                                          # Deselect the piece if clicking on an empty square or another piece of the same color
                                          if (spots[key][2] == 0) or \
                                          (turn == "white" and spots[key][2] in [ApawnW, BpawnW, CpawnW, DpawnW, EpawnW, FpawnW, GpawnW, HpawnW, LrookW, RrookW, LknightW, RknightW, LbishopW, RbishopW, queenW, kingW]) or \
                                          (turn == "black" and spots[key][2] in [ApawnB, BpawnB, CpawnB, DpawnB, EpawnB, FpawnB, GpawnB, HpawnB, LrookB, RrookB, LknightB, RknightB, LbishopB, RbishopB, queenB, kingB]):
                                                selected_piece = None
                                                selected_pos = None
                                                highlighted_moves = []


      # Calculate scores
      white_score = calculate_score(captured_black)
      black_score = calculate_score(captured_white)
      score_difference = white_score - black_score

      # Render score difference
      score_text = font.render(f"Score Difference: {score_difference}", True, BLACK)                 

      window.fill(WHITE)
      window.blit(board, (0, 0))
      for key, (x, y, piece) in spots.items():
            if piece != 0:
                  window.blit(piece, (x+25, y))
      for i in range(8):
            window.blit(letters[chr(97 + i)], (i * 80 + 65, HEIGHT - 20))
            window.blit(numbers[i + 1], (5, 560 - (i * 80) + 5))

      if selected_piece is not None:
            pygame.draw.rect(window, HIGHLIGHT, blocks[selected_pos], 3)
            for move in highlighted_moves:
                  pygame.draw.rect(window, HIGHLIGHT, blocks[move], 3)

      if score_difference > 0:
            # White is ahead
            white_score_text = font.render(('+' + str(score_difference)), True, WHITE_SCORE_COLOR)
            # Draw white score near bottom of the panel
            window.blit(white_score_text, (660, 590))
            
      elif score_difference < 0:
            # Black is ahead
            black_score_text = font.render(('+' + str(-1 * score_difference)), True, BLACK_SCORE_COLOR)
            # Draw black score near top of the panel
            window.blit(black_score_text, (660, 30))

      if promotion_needed:
            promoted_piece = promotion_popup(window, "white")
            print("Promoted to", promoted_piece)

      pygame.display.update()

pygame.quit()