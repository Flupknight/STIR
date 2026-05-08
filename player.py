import pygame

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,100))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (400,250)

    def draw(self, screen):
        screen.blit(self.image, self.rect)  