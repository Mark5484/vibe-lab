import pygame
import numpy as np
import random
import math

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("COLT Static Bloom")

# Colors: VHS-inspired, saturated teal/magenta
COLORS = [
    (0, 128, 128),  # Teal
    (255, 51, 153),  # Magenta
    (255, 191, 0),   # Amber
    (153, 51, 255),  # Purple
    (255, 102, 102)  # Light Red
]

# Add CRT scanlines overlay
scanlines = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
scanlines.fill((0, 0, 0, 100))
for y in range(0, HEIGHT, 4):
    pygame.draw.line(scanlines, (0, 0, 0, 50), (0, y), (WIDTH, y), 1)

# Add VHS noise texture
noise = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
for _ in range(10000):  # Add random noise dots
    x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    pygame.draw.circle(noise, (255, 255, 255, 10), (x, y), 1)

# Muscle-inspired silhouette (simplified torso shape)
def draw_torso(surface, x, y, size, color, degradation=0.0):
    points = [
        (x, y - size // 2),
        (x - size // 3, y),
        (x, y + size // 2),
        (x + size // 3, y)
    ]
    # Apply degradation: distort points slightly
    points = [(px + random.uniform(-degradation, degradation), py + random.uniform(-degradation, degradation)) for px, py in points]
    pygame.draw.polygon(surface, color, points)
    # Add "vein" details
    for i in range(3):
        pygame.draw.line(
            surface, 
            (min(c + 50, 255) for c in color),
            points[i],
            points[(i + 1) % 4],
            int(size * 0.05)
        )

# Main loop
def main():
    clock = pygame.time.Clock()
    running = True
    degradation = 0.0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear screen
        screen.fill((0, 0, 0))
        
        # Draw torso silhouettes with progressive degradation
        for _ in range(3):
            x, y = random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)
            size = random.randint(100, 200)
            color = random.choice(COLORS)
            draw_torso(screen, x, y, size, color, degradation)
        
        # Apply VHS noise and scanlines
        screen.blit(noise, (0, 0))
        screen.blit(scanlines, (0, 0))
        
        # Increase degradation over time
        degradation = min(degradation + 0.01, 10.0)
        
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()

if __name__ == "__main__":
    main()