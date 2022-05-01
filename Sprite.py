import pygame
class Sprite:
    def __init__(self,img,x,y,speed):
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image,(80,150))
        self.x = x
        self.y = y
        self.speed = speed
    def update(self,ev1,ev2,ev3,ev4):
        if key[ev1]:
            self.x -= self.speed
        if key[ev2]:
            self.x += self.speed
        if key[ev3]:
            self.y -= self.speed
        if key[ev4]:
            self.y += self.speed
window = pygame.display.set_mode((900,600))
player = Sprite("player.png",100,100,2)
player_2 = Sprite("player.png",250,250,4)
game = True
while game:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game = False
    key = pygame.key.get_pressed()
    player.update(pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN)
    player.update(pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s)
    window.fill((0, 0, 0))
    window.blit(player.image, (player.x, player.y))
    window.blit(player_2.image, (player_2.x, player_2.y))
    pygame.display.update()
pygame.quit()