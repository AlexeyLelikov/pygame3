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
    def __init__(self,img,x,y,speed):
        Sprite.__init__(self,img,x,y)
        self.speed = speed
class Tree(Sprite):
    def __init__(self,img,x,y):
        Sprite.__init__(self,img,x,y)
        self.image = pygame.transform.scale(self.image,(300,400))
    def changeImage(self,newimage):
        self.image = pygame.image.load(newimage)

window = pygame.display.set_mode((Screen_width,Screen_height))
player = Hero('GoAnim/b1.png',100,200,2)
tree = Tree('tree.png',400,200)
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
        player.rect.x -= player.speed
        player.image = imgPlayerGoL[Ncadr % 5]
    if key[pygame.K_RIGHT]:
        player.rect.x += player.speed
        player.image = imgPlayerGoR[Ncadr % 5]
    if collide(player.rect,tree.rect):
        tree.changeImage('GoAnim/b1.png')
    Ncadr += 1
    window.fill((0,0,0))
    window.blit(player.image,player.rect)
    window.blit(tree.image,tree.rect)
    pygame.display.update()
pygame.quit()




