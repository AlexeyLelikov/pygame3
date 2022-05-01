import pygame
Screen_width = 1280 # ширина окна
Screen_height = 720 # Высота окна

def collide(Sprite1,Sprite2):
    if ((     Sprite1.x <=  Sprite2.x  <= Sprite1.x + Sprite1.width
        and   Sprite1.y <= Sprite2.y <= Sprite1.y + Sprite1.height)
        or   (Sprite1.x <= Sprite2.x + Sprite2.width  <= Sprite1.x + Sprite1.width
        and   Sprite1.y <= Sprite2.y + Sprite2.height <= Sprite1.y + Sprite1.height)
        or   (Sprite2.x <= Sprite1.x + Sprite1.width  <= Sprite2.x + Sprite2.width
        and   Sprite2.y <= Sprite1.y <= Sprite2.y + Sprite2.height)
        or   (Sprite2.x <= Sprite1.x <= Sprite2.x + Sprite2.width
        and   Sprite2.y <= Sprite1.y + Sprite1.height <= Sprite2.y + Sprite2.height)):
        return  True
    else:
        return False
class Sprite: # Класс родитель
    def __init__(self, img, x, y):
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(topleft = (x,y))
class Hero(Sprite):
    def __init__(self,img,x,y,speedx,speedy):
        Sprite.__init__(self,img,x,y)
        self.speedx = speedx
        self.speedy = speedy
        self.jump = 5
class Platform(Sprite):
    def __init__(self,img,x,y,speedy,time):
        Sprite.__init__(self,img,x,y)
        self.speedy = speedy
        self.time = time
class Const:
    def __init__(self,value):
        self.value = value

# Create object
g = Const(1)
window = pygame.display.set_mode((Screen_width,Screen_height))
player = Hero('GoAnim/b1.png',500,100,2,0)
pl = Platform('ground.png',400,500,1,0)
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
        player.rect.x -= player.speedx
        player.image = imgPlayerGoL[Ncadr % 5]
    if key[pygame.K_RIGHT]:
        player.rect.x += player.speedx
        player.image = imgPlayerGoR[Ncadr % 5]
    if collide(player.rect,pl.rect):
        player.speedy = 0
    else:
        player.speedy += g.value
    player.rect.y += player.speedy
    Ncadr += 1
    window.fill((0,0,0))
    window.blit(player.image,player.rect)
    window.blit(pl.image,pl.rect)
    pygame.display.update()
pygame.quit()




