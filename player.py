import pygame

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,100))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (400,250)
        self.xPos = 400
        self.yPos = 250

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def update(self):
        # moving controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.xPos -= 1
        if keys[pygame.K_d]:
            self.xPos += 1
        
        self.rect.center = (self.xPos, self.yPos)