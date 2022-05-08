import pygame
import lib_collide

class Sprite(pygame.sprite.Sprite): # Класс родитель
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(topleft = (x,y))
class Player(Sprite):
    pass