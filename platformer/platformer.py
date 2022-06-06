import pygame
import random
WorldWidth = 1800 # ширина игрового мира
WorldHeight = 1200 # высота игрового мира
ScreenWidth = 900 # ширина окна
ScreenHeight = 600 # высота окна

class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
    def update(self,player):
        if player.rect.x < WorldWidth - ScreenWidth / 2 and player.rect.x > ScreenWidth / 2:
            self.x = int(ScreenWidth / 2) - player.rect.x
        if player.rect.y < WorldHeight - ScreenHeight / 2 and player.rect.y > ScreenHeight / 2:
            self.y = int(ScreenHeight / 2) - player.rect.y



