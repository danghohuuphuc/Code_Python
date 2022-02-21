# Import library
import sys, pygame

# initialize the game
#khoi tao khung kich thuoc game
size = width, height = 320, 240

# khoi tao toc do game
speed = [2, 2]

# khoi tao mau sac khung
black = 0, 0, 0

# dat kich thuoc man hinh game
screen = pygame.display.set_mode(size)

# tai anh ball
ball = pygame.image.load("intro_ball.gif")
# tao khung game
ballrect = ball.get_rect()

# tao vong lap trong game
while 1:

    #dieu kien de thoat vong lap 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    # di chuyen cua trai banh
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    
    #khoi tao man hinh
    screen.fill(black)
    # lay bien tao man hinh
    screen.blit(ball, ballrect)
    pygame.display.flip()