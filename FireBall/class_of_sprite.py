import pygame
import lib_collide
import random

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
        if lib_collide.collideG(self,GroupFireBall):
            self.game = False
        self.cadr += 1
class Fireball(Sprite):
    def __init__(self,img,speedy,Anim):
        super().__init__(img,random.randint(1,1200),0)
        self.start_speed = speedy
        self.speedy = speedy
        self.Anim = Anim
        self.cadr = 0
    def update(self,g):
        if self.rect.y < 700:
            self.speedy += g.value
            self.rect.y += self.speedy
            self.image = self.Anim[self.cadr % 4]
        else:
            self.rect.x = random.randint(1,1200)
            self.rect.y = 0
            self.speedy = self.start_speed
        self.cadr += 1
class Const:
    def __init__(self,value):
        self.value = value








