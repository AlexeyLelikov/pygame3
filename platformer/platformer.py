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

class Sprite(pygame.sprite.Sprite):
    def __init__(self,x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(topleft = (x, y))

class Player(Sprite):
    def __init__(self, x, y, img, speed):
        super().__init__(x, y, img)
        self.speed = speed
        self.cadr = 0
    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.rect.x += speed
        elif key[pygame.K_LEFT]:
            self.rect.x -= speed
        elif key[pygame.K_UP]:
            self.rect.y -= speed
        elif key[pygame.K_DOWN]:
            self.rect.y += speed

w = pygame.display.set_mode((ScreenWidth,ScreenHeight))
world = pygame.Surface((WorldWidth,WorldHeight))
player = Player(900,600,'player.jpg',3)
camera = Camera()
bg_sprite = Sprite(0,0,'bg.png')
bg_sprite.image = pygame.transform.scale(bg_sprite.image,(1800,1200))
game = True
while game:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game = False
    player.update()
    camera.update(player)
    world.fill((0,0,0))
    world.blit(bg_sprite.image,bg_sprite.rect)
    world.blit(player.image,player.rect)
    pygame.display.update()
pygame.quit()






