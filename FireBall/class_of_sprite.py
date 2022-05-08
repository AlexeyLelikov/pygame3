import pygame
import lib_collide

class Sprite(pygame.sprite.Sprite): # Класс родитель
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(topleft = (x,y))
class Player(Sprite):
    def __init__(self,img,x,y,speedx,animR,animL):
        Sprite.__init__(self,img,x,y)
        self.speedx = speedx
        self.AnimGoL = animL
        self.AnimGoR = animR
        self.cadr = 0
        self.game = True
    def update(self,key,GroupFireBall):
        if key[pygame.K_LEFT]:
            self.x -= self.speed
            self.image = imgPlayerGoL[self.cadr % 5]
        if key[pygame.K_RIGHT]:
            self.x += self.speed
            self.image = imgPlayerGoR[self.cadr % 5]
        if collideG(self.rect,GroupFireBall):
            self.game = False
        self.cadr += 1






