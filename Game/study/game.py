# import library
from cProfile import run
from operator import iconcat
import pygame, sys

#import module
from pygame.locals import *

# initialize the game
pygame.init()

# khởi tạo khung hình game
screen = pygame.display.set_mode((800, 600))

# Thay đổi caption của khung game
pygame.display.set_caption("Hello world")

# Thay đổi icon của khung game
icon = pygame.image.load("pikachu.png")
pygame.display.set_icon(icon)

# vòng lập game
while True:
    # điều kiện để thoát khung hình game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    # update dữ liệu cần thiết
    pygame.display.update()