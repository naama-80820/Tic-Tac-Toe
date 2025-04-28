import pygame
from constants import *

class Board:
    def __init__(self):
        self.board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]

    def available_square(self, row, col):
        return self.board[row][col] is None

    def mark_square(self, row, col, symbol):
        self.board[row][col] = symbol

    def is_full(self):
        for row in self.board:
            for cell in row:
                if cell is None:
                    return False
        return True

    def clear_board(self):
        self.board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]

    def draw(self, screen):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                pygame.draw.rect(screen, LINE_COLOR, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                                 LINE_WIDTH)

                if self.board[row][col] == 'X':
                    pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE, row * SQUARE_SIZE),
                                     ((col + 1) * SQUARE_SIZE, (row + 1) * SQUARE_SIZE), CROSS_WIDTH)
                    pygame.draw.line(screen, CROSS_COLOR, ((col + 1) * SQUARE_SIZE, row * SQUARE_SIZE),
                                     (col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE), CROSS_WIDTH)
                elif self.board[row][col] == 'O':
                    pygame.draw.circle(screen, CIRCLE_COLOR,
                                       (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                       CIRCLE_RADIUS, CIRCLE_WIDTH)
