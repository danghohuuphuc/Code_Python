import pygame, sys
pygame.init()

screen_width=700
screen_height=400
screen = pygame.display.set_mode((screen_width, screen_height))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()