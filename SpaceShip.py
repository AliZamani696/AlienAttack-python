import pygame



class SpaceShip:
    def __init__(self,screen):
        self.screen = screen
        self.Image = pygame.image.load("images/hiclipart.bmp");
        self.rect = self.Image.get_rect()
        self.recty = self.Image.
        self.screen_rect = screen.get_rect()
        self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        self.rect[3]+=1
        self.screen.blit(self.Image,self.rect)
