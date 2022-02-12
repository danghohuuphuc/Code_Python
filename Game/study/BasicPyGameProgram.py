# import library
import pygame
pygame.init()

# set up the drawing window
screen = pygame.display.set_mode([500, 500])



# the main game loop 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

screen.fill((255, 255, 255))
