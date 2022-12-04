import pygame
import random
import sys
from pygame.locals import *
import time


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60


class Player():
    pass


class Enemy():
    pass


class World():
    def __init__(self):
        self.reset()

    def reset(self):
        self.GameOver = False

    def end(self):
        return self.GameOver
    
    def update(self):
        pass

    def draw(self):
        pass



pygame.init()
running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tiny Spark')
surface = pygame.Surface(screen.get_size())
surface = surface.convert()


font = pygame.font.Font(None, 48)


def quit():
    pygame.quit()
    sys.exit()


def Click_to_play():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                return


def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, WHITE)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


drawText('Tiny Spark', font, screen, (210), (230))
drawText('Press a key to start', font, screen, (150), (268))
pygame.display.update()
Click_to_play()
while running:
    clock.tick(FPS)
    surface.fill(BLACK)
    screen.blit(surface, (0, 0))
    drawText('*Playing*', font, screen, (210), (230))

    pygame.display.update()
