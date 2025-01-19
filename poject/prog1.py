import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Beyblade")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# Beyblade properties
beyblade_radius = 50
beyblade_center = (width // 2, height // 2)
angle = 0
rotation_speed = 5

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(black)

    # Calculate new angle
    angle += rotation_speed
    angle %= 360

    # Draw beyblade
    for i in range(3):
        theta = math.radians(angle + i * 120)
        x = beyblade_center[0] + beyblade_radius * math.cos(theta)
        y = beyblade_center[1] + beyblade_radius * math.sin(theta)
        pygame.draw.line(screen, red if i % 2 == 0 else blue, beyblade_center, (x, y), 5)

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()