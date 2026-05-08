
import pygame

pygame.display.init
screen = pygame.display.set_mode((800, 500))

runing = bool(True)


while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
    screen.fill((141, 141, 141))
    pygame.display.flip()


pygame.quit()