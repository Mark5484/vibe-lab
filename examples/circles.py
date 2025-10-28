"""
Generative Art Example: Colorful Circles
Creates a static visual art piece with overlapping circles in harmonious colors.
"""
import pygame
import random
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.colors import generate_palette, hsv_to_rgb
from src.geometry import circle_points


def draw_circles(screen, width, height):
    """Draw overlapping circles with varying sizes and colors."""
    # Generate a harmonious color palette
    base_hue = random.randint(0, 360)
    palette = generate_palette(base_hue=base_hue, count=8, saturation=0.7, value=0.85)
    
    # Draw background
    bg_color = hsv_to_rgb(base_hue, 0.1, 0.95)
    screen.fill(bg_color)
    
    # Create circles with varying sizes
    num_circles = 50
    for i in range(num_circles):
        # Random position
        x = random.randint(0, width)
        y = random.randint(0, height)
        
        # Random radius
        radius = random.randint(20, 150)
        
        # Pick a color from palette
        color = palette[i % len(palette)]
        
        # Draw with transparency
        surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        alpha = random.randint(30, 100)
        color_with_alpha = (*color, alpha)
        pygame.draw.circle(surface, color_with_alpha, (radius, radius), radius)
        screen.blit(surface, (x - radius, y - radius))


def main():
    """Main function to run the sketch."""
    # Initialize Pygame
    pygame.init()
    
    # Set up display
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Vibe Lab - Generative Circles")
    
    # Create the art
    draw_circles(screen, width, height)
    pygame.display.flip()
    
    # Save the image
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'circles.png')
    pygame.image.save(screen, output_path)
    print(f"Saved artwork to: {output_path}")
    
    # Main loop
    running = True
    print("Press SPACE to generate new art, or Q to quit")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_SPACE:
                    # Generate new art
                    draw_circles(screen, width, height)
                    pygame.display.flip()
                    # Save the new image
                    pygame.image.save(screen, output_path)
                    print(f"Generated new artwork: {output_path}")
    
    pygame.quit()


if __name__ == "__main__":
    main()
