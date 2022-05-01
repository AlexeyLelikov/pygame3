import pygame
Screen_width = 1280 # ширина окна
Screen_height = 720 # Высота окна

class Sprite:
    def __init__(self,img,x,y,speed):
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image,(80,150))
        self.x = x
        self.y = y
        self.speed = speed

window = pygame.display.set_mode((Screen_width,Screen_height))
player = Sprite('GoAnim/b1.png',100,100,2)
clock = pygame.time.Clock()
imgPlayerGoR = [pygame.image.load('GoAnim/b1.png'),
                pygame.image.load('GoAnim/b2.png'),
                pygame.image.load('GoAnim/b3.png'),
                pygame.image.load('GoAnim/b4.png'),
                pygame.image.load('GoAnim/b5.png')]
imgPlayerGoL = []
for img in imgPlayerGoR:
    imgPlayerGoL.append(pygame.transform.flip(img,True,False))
Ncadr = 0
game = True
while game:
    clock.tick(15)
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game = False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.x -= player.speed
        player.image = imgPlayerGoL[Ncadr % 5]
    if key[pygame.K_RIGHT]:
        player.x += player.speed
        player.image = imgPlayerGoR[Ncadr % 5]
    Ncadr += 1
    window.fill((0,0,0))
    window.blit(player.image,(player.x,player.y))
    pygame.display.update()
pygame.quit()