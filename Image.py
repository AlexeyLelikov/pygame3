import pygame
window = pygame.display.set_mode((900,600))
player = pygame.image.load('player.png')
player_2 = pygame.image.load('player.png')
player = pygame.transform.scale(player,(80,150))
game = True
x = 100
y = 100
while game:
    Listevent = pygame.event.get()
    for ev in Listevent:
        if ev.type == pygame.QUIT:
            game = False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        x -= 1
    if key[pygame.K_RIGHT]:
        x += 1
    if key[pygame.K_UP]:
        y -= 1
    if key[pygame.K_DOWN]:
        y += 1
    window.fill((0,0,0))
    window.blit(player,(x,y))
    pygame.display.update()
pygame.quit()