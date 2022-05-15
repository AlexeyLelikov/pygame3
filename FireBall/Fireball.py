import pygame
from class_of_sprite import Const,Fireball,Player

# Создание анимации Fireball
ImgAnimFireBall = [pygame.image.load('GoAnim/fireball.png'),
                   pygame.image.load('GoAnim/fireball1.png'),
                   pygame.image.load('GoAnim/fireball2.png'),
                   pygame.image.load('GoAnim/fireball3.png')]
for i in range(len(ImgAnimFireBall)):
    scale = pygame.transform.scale(ImgAnimFireBall[i],(180,65))
    ImgAnimFireBall[i] = pygame.transform.rotate(scale,-90)
# Создаем анимацию Player
imgPlayerGoR = [pygame.image.load('GoAnim/b1.png'),
                pygame.image.load('GoAnim/b2.png'),
                pygame.image.load('GoAnim/b3.png'),
                pygame.image.load('GoAnim/b4.png'),
                pygame.image.load('GoAnim/b5.png')]
imgPlayerGoL = []
for img in imgPlayerGoR:
    imgPlayerGoL.append(pygame.transform.flip(img,True,False))

window = pygame.display.set_mode(1280,700)
clock = pygame.time.Clock()
g = Const(1)


