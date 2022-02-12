#import library
from cProfile import run
from cmath import rect
from json.encoder import ESCAPE
from sys import platlibdir
import pygame

from pygame.locals import *
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

pygame.display.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
player = Player()
# tạo một vật thể hình với màu
surf = pygame.Surface((50, 50))
# lấy kích thước của vật thể
rect = surf.get_rect()

# the main game loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    screen.fill((0, 0, 0))

  
    # vẽ hình tròn
    screen.blit(player.surf, (screen_width/2, screen_height/2))
    pygame.display.flip()