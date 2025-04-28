import pygame
import sys
from constants import *
from board import Board
from game import Game
from menu import Menu

# פונקציה להצגת כפתור "התחל משחק חדש"
def draw_new_game_button(screen):
    button_font = pygame.font.SysFont(None, 40)
    button_text = button_font.render("New Game", True, (255, 255, 255))
    button_rect = button_text.get_rect(center=(WIDTH // 2, HEIGHT // 1.1))
    pygame.draw.rect(screen, (66, 66, 66), button_rect.inflate(20, 20))
    screen.blit(button_text, button_rect)
    return button_rect

# פונקציה לבדוק אם המשתמש לחץ על כפתור "התחל משחק חדש"
def check_restart_button(event, button_rect, game, board):
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouseX, mouseY = event.pos
        if button_rect.collidepoint(mouseX, mouseY):  # בודק אם לחצו על הכפתור
            game.game_over = False
            board.clear_board()  # מנקה את הלוח ומחפש משחק חדש
            return True
    return False
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tic Tac Toe')

    menu = Menu(screen)
    menu.start_screen()  # מציג את מסך הפתיחה

    board = Board()
    game = Game(board)  # אין צורך בשחקנים

    while game.running:
        screen.fill((0, 0, 0))  # מנקה את המסך

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

            if event.type == pygame.MOUSEBUTTONDOWN and not game.game_over:
                mouseX, mouseY = event.pos
                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE
                game.make_move(clicked_row, clicked_col)

            if game.game_over:
                button_rect = draw_new_game_button(screen)
                if check_restart_button(event, button_rect, game, board):
                    game.game_over = False
                    board.clear_board()

        board.draw(screen)
        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
