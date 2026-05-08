
import pygame

pygame.display.init
screen = pygame.display.set_mode((640, 480))

runing = bool(True)


while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False