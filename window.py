import pygame
window = pygame.display.set_mode((900,600))
game = True
while game:
    Listevent = pygame.event.get()
    for ev in Listevent:
        if ev.type == pygame.QUIT:
            game = False
pygame.quit()
