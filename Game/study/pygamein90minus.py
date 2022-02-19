#Import library
import pygame
import os

# init the win
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First game!")

WHITE = 255, 255, 255
BLACK = 0, 0 , 0
RED = 255, 0, 0
YELLOW = 255, 255, 0

# tạo khung khoảng cách ở giữa của 2 máy bay
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
#tạo viên đạn
BULLET_VEL = 7
MAX_BULLETS = 3
# init fps game
FPS = 60
# bước di chuyển
VEL = 5


# Chiều dài chiều rộng của SpaceShip
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

# load image spaceship
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE =pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))

# Thay đổi kích thước của hình ảnh bằng pygame.transform.scale
# Xoay hình ảnh bằng pygame.transform.rotate
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

# Load Space 
SPACE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')))
#  
def draw_window(red, yellow, red_bullets, yellow_bullets):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()

# yellow move
def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: # move left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 10:
        yellow.y += VEL

# red move
def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH + 15: # move left
        red.x += VEL
    if keys_pressed[pygame.K_LEFT] and red.x + VEL > BORDER.x + 35:
        red.x -= VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 10:
        red.y += VEL

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet )
# hàm chính
def main():
    # Hàm pygame.Rect() dùng để lưu vị trí của một vật thể
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []
    # đặt biến khóa fps
    fpsClock = pygame.time.Clock()
    run = True
    while run:
        #sử dụng biến khóa fps
        fpsClock.tick(FPS)
        # vòng lập để thoát sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #chuyển động của viên đạn khi ấn nút
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5 )
                    red_bullets.append(bullet)

        # move
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets)
    pygame.quit()
if __name__ == "__main__":
    main()