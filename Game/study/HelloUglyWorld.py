import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Hello Ugly World")
icons = pygame.image.load("pikachu.png")
pygame.display.set_icon(icons)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()