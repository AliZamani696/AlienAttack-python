import pygame as GAME_ENGINE
from Setting import Setting
from SpaceShip import SpaceShip

def init():
        GAME_ENGINE.init()
        setting = Setting()
        Ship = SpaceShip(setting.screen)
        GAME_ENGINE.display.set_caption("Alien Attack")
        spaceShip = GAME_ENGINE.image.load ("./images/hiclipart.bmp")
        running = True
        while running:
                for event in GAME_ENGINE.event.get():
                        if event.type == GAME_ENGINE.QUIT:
                                running = False

                #---------------game logic---------------

                setting.Scrolling_Background()
                Ship.blitme()
                GAME_ENGINE.display.update()
init()
