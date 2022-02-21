#import library
import pygame, sys
from pygame.locals import *

# initlizatie the game
pygame.init()

# đặt tốc độ khung hình và khóa nó
FPS = 30
fpsClock = pygame.time.Clock()

# set up the window
screen = pygame.display.set_mode((400, 300))

# Set caption
pygame.display.set_caption("Animation")

# set color white
WHITE = (255, 255, 255)

# load image cat
catImg = pygame.image.load("cat.png")

# position cat
catx = 10
caty = 10

# direction cat
direction = 'right'

# the main game loop
while True:
    #set color khung hinh
    screen.fill(WHITE)
     
    # cat move
    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction ='right'
    screen.blit(catImg, (catx, caty)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    pygame.display.update()
    fpsClock.tick(FPS)