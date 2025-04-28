import pygame
import sys
from constants import WIDTH, HEIGHT

class Menu:
    def __init__(self, screen):
        self.screen = screen

    def start_screen(self):
        font = pygame.font.SysFont(None, 60)
        title_text = font.render("Tic Tac Toe", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))

        button_font = pygame.font.SysFont(None, 40)
        button_text = button_font.render("Start Game", True, (255, 255, 255))
        button_rect = button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        running = True
        while running:
            self.screen.fill((28, 170, 156))

            self.screen.blit(title_text, title_rect)

            pygame.draw.rect(self.screen, (66, 66, 66), button_rect.inflate(20, 20))
            self.screen.blit(button_text, button_rect)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        return  # יחזור להתחלת המשחק
