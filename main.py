import pygame
import random
import sys
import button

# constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

FPS = 60
ENEMY_SPAWN_RATE = 2
ENEMY_MIN_SIZE = 4
ENEMY_MAX_SIZE = 15
ENEMY_MIN_SPEED = 2
ENEMY_MAX_SPEED = 10
PLAYER_SPEED = 3
PLAYER_SIZE = 10
PLAYER_MAX_UP = 150

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHTBLUE = (202, 228, 241)

# пишем текст
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, WHITE)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def run():
    pygame.init()
    pygame.display.set_caption("Tiny Spark")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Загрузка изображений в меню
    start_img = pygame.image.load('images\menu\start_btn.png').convert_alpha()
    setting_img = pygame.image.load('images\menu\setting_btn.png').convert_alpha()
    exit_img = pygame.image.load('images\menu\exit_btn.png').convert_alpha()
    shop_img = pygame.image.load('images\menu\shop.png').convert_alpha()

    # Устанавливаем кнопки
    start_button = button.Button(420, 200, start_img, 1.6)
    setting_button = button.Button(420, 290, setting_img, 1.6)
    exit_button = button.Button(420, 380, exit_img, 1.6)
    shop_button = button.Button(860, 560, shop_img, 0.8)
    clock = pygame.time.Clock()
    surface = pygame.Surface(screen.get_size())
    running = True
    while running:
        screen.fill(LIGHTBLUE)
        clock.tick(FPS)
        # Отрисовка кнопок через файл button.py
        start_button.draw(screen)
        setting_button.draw(screen)
        exit_button.draw(screen)
        shop_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False     
        pygame.display.update()

        
if __name__ == '__main__':
    run()