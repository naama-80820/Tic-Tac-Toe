import pygame

# גודל החלון
WIDTH, HEIGHT = 600, 600

# הלוח
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
LINE_WIDTH = 10

# סמלים
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 20
SPACE = SQUARE_SIZE // 4

# צבעים
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# פונטים
pygame.font.init()
FONT = pygame.font.SysFont(None, 60)
