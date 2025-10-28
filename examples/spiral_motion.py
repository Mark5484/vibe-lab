"""
Motion Sketch: Animated Spiral
Creates an animated spiral with moving particles in colorful patterns.
"""
import pygame
import math
import random
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.colors import generate_palette, hsv_to_rgb
from src.geometry import spiral_points, lerp


class Particle:
    """A particle that moves along a spiral path."""
    
    def __init__(self, center_x, center_y, index, total, start_radius, end_radius, rotations, color):
        self.center_x = center_x
        self.center_y = center_y
        self.progress = index / total
        self.speed = random.uniform(0.001, 0.003)
        self.start_radius = start_radius
        self.end_radius = end_radius
        self.rotations = rotations
        self.color = color
        self.size = random.randint(3, 8)
    
    def update(self):
        """Update particle position."""
        self.progress = (self.progress + self.speed) % 1.0
    
    def get_position(self):
        """Calculate current position on spiral."""
        angle = self.progress * self.rotations * 2 * math.pi
        radius = self.start_radius + (self.end_radius - self.start_radius) * self.progress
        x = self.center_x + radius * math.cos(angle)
        y = self.center_y + radius * math.sin(angle)
        return (x, y)
    
    def draw(self, screen):
        """Draw the particle."""
        x, y = self.get_position()
        # Fade alpha based on progress
        alpha = int(255 * (1 - self.progress * 0.5))
        surface = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
        color_with_alpha = (*self.color, alpha)
        pygame.draw.circle(surface, color_with_alpha, (self.size, self.size), self.size)
        screen.blit(surface, (int(x - self.size), int(y - self.size)))


def main():
    """Main function to run the animated sketch."""
    # Initialize Pygame
    pygame.init()
    
    # Set up display
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Vibe Lab - Animated Spiral")
    clock = pygame.time.Clock()
    
    # Generate color palette
    base_hue = random.randint(0, 360)
    palette = generate_palette(base_hue=base_hue, count=6, saturation=0.8, value=0.9)
    bg_color = hsv_to_rgb(base_hue, 0.05, 0.1)
    
    # Create particles
    center_x, center_y = width // 2, height // 2
    num_particles = 100
    particles = []
    
    for i in range(num_particles):
        color = palette[i % len(palette)]
        particle = Particle(
            center_x, center_y, i, num_particles,
            start_radius=10, end_radius=250, rotations=5, color=color
        )
        particles.append(particle)
    
    # Animation variables
    time_elapsed = 0
    running = True
    
    print("Press SPACE to regenerate, or Q to quit")
    
    # Main loop
    while running:
        dt = clock.tick(60) / 1000.0  # Delta time in seconds
        time_elapsed += dt
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_SPACE:
                    # Regenerate with new colors
                    base_hue = random.randint(0, 360)
                    palette = generate_palette(base_hue=base_hue, count=6, saturation=0.8, value=0.9)
                    bg_color = hsv_to_rgb(base_hue, 0.05, 0.1)
                    
                    particles = []
                    for i in range(num_particles):
                        color = palette[i % len(palette)]
                        particle = Particle(
                            center_x, center_y, i, num_particles,
                            start_radius=10, end_radius=250, rotations=5, color=color
                        )
                        particles.append(particle)
                    print("Regenerated with new colors")
        
        # Clear screen with fade effect for trail
        fade_surface = pygame.Surface((width, height))
        fade_surface.fill(bg_color)
        fade_surface.set_alpha(30)
        screen.blit(fade_surface, (0, 0))
        
        # Update and draw particles
        for particle in particles:
            particle.update()
            particle.draw(screen)
        
        # Draw center point
        pygame.draw.circle(screen, (255, 255, 255), (center_x, center_y), 3)
        
        pygame.display.flip()
    
    pygame.quit()


if __name__ == "__main__":
    main()
