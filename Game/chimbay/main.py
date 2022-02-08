import pygame

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title  and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("battleship.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("robot.png")
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Game Loop
running = True
while running:

    # RGB - red, green, blue
    screen.fill((0, 0, 0))

    playerY -= 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player(playerX, playerY  )
    pygame.display.update()