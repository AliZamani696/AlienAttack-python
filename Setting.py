import pygame

class Setting:
        def __init__(self):
                self.screen_height = 1200
                self.screen_width = 800
                self.screen = pygame.display.set_mode((self.screen_height,self.screen_width))
                self.BackGround = pygame.image.load("images/background/BG.jpg")
                #self.background_x = self.screen_width
                self.background_y = self.screen_height
                self.bg_y = 0
                #self.bg_x = 0
                self.speed = 0.4
        def Scrolling_Background(self):
                self.bg_y -= self.speed
                if self.bg_y <= -self.background_y:
                        self.bg_y = 0
                self.screen.blit(self.BackGround,(0,self.bg_y))
                self.screen.blit(self.BackGround,(0,self.bg_y+self.background_y))
