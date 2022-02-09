# import library
from dis import dis
import re
import pygame, sys
from pygame.locals import *

# Khởi tạo 
pygame.init()

# Khởi tạo khung hình game
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)

# Thay đổi caption
pygame.display.set_caption("game 1")

# Thay đổi icon khung game
icongame1 = pygame.image.load("pikachu.png")
pygame.display.set_icon(icongame1)

# cài đặt màu săc
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# draw on the surface object
DISPLAYSURF.fill(white)

# Vẽ hình năm cạnh
pygame.draw.polygon(DISPLAYSURF, green, ((146, 0), (291, 106), 
    (236, 277), (56, 277), (0, 106)))

# Vẽ đường thẳng
pygame.draw.line(DISPLAYSURF, blue, (60, 60), (120,60) ,10)
pygame.draw.line(DISPLAYSURF, blue, (120, 60), (60, 120), 10)
pygame.draw.line(DISPLAYSURF, blue, (60, 120), (120, 120), 10)

# Vẽ hình tròn
pygame.draw.circle(DISPLAYSURF, blue, (300, 50), 20, 0)

# Vẽ hình elcip
pygame.draw.ellipse(DISPLAYSURF, red, (300, 250, 40, 80), 5)

# Vẽ Hình chữ nhật
pygame.draw.rect(DISPLAYSURF, red, (200, 150, 100, 50))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = black
pixObj[482][382] = black
pixObj[484][384] = black
pixObj[486][386] = black
pixObj[488][388] = black
del pixObj

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # update data
    pygame.display.update()