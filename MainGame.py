# import pygame as GAME_ENGINE



# def init():
#         GAME_ENGINE.init()

#         screen = GAME_ENGINE.display.set_mode((1200,800))
#         GAME_ENGINE.display.set_caption("Alien Attack")
#         background = GAME_ENGINE.image.load("./images/background/BG.jpg")
#         background_y = background.get_height()
#         background_x = background.get_width()
#         bg_y = 0
#         bg_x = 0
#         speed = 0.4
#         running = True
#         while running:
#                 for event in GAME_ENGINE.event.get():
#                         if event.type == GAME_ENGINE.QUIT:
#                                 running = False

#                 #---------------game logic---------------
#                 bg_y -= speed
#                 if bg_y <= -background_y:
#                         bg_y = 0
#                 screen.blit(background,(0,bg_y))
#                 screen.blit(background,(0,bg_y+background_y))
#                 GAME_ENGINE.display.update()
# init()
