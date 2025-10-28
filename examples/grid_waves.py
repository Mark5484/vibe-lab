"""
Generative Art Example: Grid Waves
Creates flowing wave patterns on a grid with dynamic colors.
"""
import pygame
import math
import random
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.colors import generate_palette, interpolate_color
from src.geometry import grid_points


def draw_grid_waves(screen, width, height, time_offset=0):
    """Draw a grid of circles with wave-like size and color variations."""
    # Grid parameters
    cols, rows = 30, 20
    padding = 50
    grid_width = width - padding * 2
    grid_height = height - padding * 2
    
    # Generate color palette
    base_hue = random.randint(0, 360)
    palette = generate_palette(base_hue=base_hue, count=5, saturation=0.7, value=0.85)
    
    # Clear screen
    screen.fill((20, 20, 30))
    
    # Get grid points
    points = grid_points(padding, padding, grid_width, grid_height, cols, rows)
    
    # Draw each point
    for i, (x, y) in enumerate(points):
        # Calculate wave based on position and time
        col = i % cols
        row = i // cols
        
        # Multiple wave sources for interesting patterns
        wave1 = math.sin((x / 50) + time_offset) * 0.5
        wave2 = math.cos((y / 50) + time_offset * 1.3) * 0.5
        wave3 = math.sin((x + y) / 70 + time_offset * 0.7) * 0.5
        
        combined_wave = (wave1 + wave2 + wave3) / 3
        
        # Map wave to radius
        min_radius = 2
        max_radius = 15
        radius = min_radius + (max_radius - min_radius) * (combined_wave + 1) / 2
        
        # Map wave to color
        color_index = int((combined_wave + 1) / 2 * (len(palette) - 1))
        color_index = max(0, min(len(palette) - 1, color_index))
        
        # Interpolate between adjacent colors for smooth transition
        if color_index < len(palette) - 1:
            factor = ((combined_wave + 1) / 2 * (len(palette) - 1)) % 1
            color = interpolate_color(palette[color_index], palette[color_index + 1], factor)
        else:
            color = palette[color_index]
        
        # Draw circle
        pygame.draw.circle(screen, color, (int(x), int(y)), int(radius))


def main():
    """Main function to run the sketch."""
    # Initialize Pygame
    pygame.init()
    
    # Set up display
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Vibe Lab - Grid Waves")
    clock = pygame.time.Clock()
    
    # Animation variables
    time_offset = 0
    animate = True
    running = True
    
    print("Press SPACE to toggle animation, R to randomize, or Q to quit")
    
    # Main loop
    while running:
        dt = clock.tick(60) / 1000.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_SPACE:
                    animate = not animate
                    print(f"Animation {'enabled' if animate else 'paused'}")
                elif event.key == pygame.K_r:
                    time_offset = random.random() * 10
                    print("Randomized pattern")
        
        # Update animation
        if animate:
            time_offset += dt * 2
        
        # Draw
        draw_grid_waves(screen, width, height, time_offset)
        
        pygame.display.flip()
    
    pygame.quit()


if __name__ == "__main__":
    main()
