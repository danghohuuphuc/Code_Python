import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
iconpikachu = pygame.image.load("pikachu.png")
pygame.display.set_icon(iconpikachu)

pygame.display.set_caption("Hello Ugly World")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

fontObj = pygame.font.Font('FreeSansBold.ttf', 32)
textSurfaceObj = fontObj.render("hello world!", True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)
# the main game loop
while True:
    screen.fill(WHITE)
    screen.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()