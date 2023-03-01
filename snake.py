import pygame

# Initialize pygame
pygame.init()

# Set the window size
window_size = (400, 400)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Snake")

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the game state

    # Draw the screen
    screen.fill((0, 0, 0))  # Clear the screen
    pygame.display.flip()  # Update the display

# Quit pygame
pygame.quit()
