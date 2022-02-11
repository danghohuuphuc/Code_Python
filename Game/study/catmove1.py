# import library
import pygame, sys
from pygame.locals import *

# khoi tao game
pygame.init()

# set fps game
FPS = 500
fpsClock = pygame.time.Clock()
#khoi tao khung game
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Animation")

WHITE = (255, 255, 255)

# load anh cat and move
catImg = pygame.image.load("cat.png")
catX = 10
catY = 10
direction = 'right'

# the main game loop
while True:

    # set nen background
    screen.fill(WHITE)

    #cat move
    if direction == 'right':
        catX += 5
        if catX == 735:
            direction = 'down'
    elif direction == 'down':
        catY += 50
        direction = 'left'
    elif direction == 'left':
        catX -= 5
        if catX == 5:
            direction = 'up'
    elif direction == 'up':
        catY += 50
        direction = 'right'
    

    # load date cat
    screen.blit(catImg, (catX, catY))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)