import pygame
from constants import *


class Game:
    def __init__(self, board):
        self.board=board
        self.running=True
        self.game_over=False
        self.turn='X'  # התור מתחיל ב-X

    def make_move(self, row, col):
        if self.board.available_square(row, col) and not self.game_over:
            current_player=self.turn  # קבע את השחקן הנוכחי (X או O)
            self.board.mark_square(row, col, current_player)

            # הפעלת הצליל
            pygame.mixer.Sound(
                r"C:\Users\מאירה\Documents\נעמה\תכנות\github-repositories\Tic Tac Toe\src\sounds\pikon.mp3").play()

            if self.check_winner(current_player):
                self.game_over=True
                pygame.mixer.Sound(
                    r"C:\Users\מאירה\Documents\נעמה\תכנות\github-repositories\Tic Tac Toe\src\sounds\tyaran.mp3").play()
                self.display_message(f"{current_player} Wins!")
            elif self.board.is_full():
                self.display_message("It's a Tie!")
                self.game_over=True
            else:
                self.turn='O' if self.turn == 'X' else 'X'  # שינוי תור

    def check_winner(self, symbol):
        # בדיקת שורות
        for row in self.board.board:
            if all(cell == symbol for cell in row):
                return True
        # בדיקת עמודות
        for col in range(BOARD_COLS):
            if all(self.board.board[row][col] == symbol for row in range(BOARD_ROWS)):
                return True
        # בדיקת אלכסון ראשון
        if all(self.board.board[i][i] == symbol for i in range(BOARD_ROWS)):
            return True
        # בדיקת אלכסון שני
        if all(self.board.board[i][BOARD_COLS - 1 - i] == symbol for i in range(BOARD_ROWS)):
            return True
        return False

    def display_message(self, message):
        text=FONT.render(message, True, (255, 255, 255))
        rect=text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen=pygame.display.get_surface()
        screen.blit(text, rect)
        pygame.display.update()
        pygame.time.delay(3000)

    def reset_game(self):
        self.board.clear_board()
        self.game_over=False
        self.turn='X'  # מתחילים מחדש עם X
