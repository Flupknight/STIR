# importing stuff
import pygame
import player


# init sprites
all_sprites = pygame.sprite.Group()
Bob = player.player()
all_sprites.add(Bob)

# init display
pygame.display.init
screen = pygame.display.set_mode((800, 500))

# game loop
runing = bool(True)

while runing:
    # off button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
    
    #update screen
    screen.fill((141, 141, 141))
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()


pygame.quit()