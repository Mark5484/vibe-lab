"""
Geometric utilities for generative art
"""
import math
import random


def circle_points(center_x, center_y, radius, num_points):
    """
    Generate points around a circle.
    
    Args:
        center_x: X coordinate of center
        center_y: Y coordinate of center
        radius: Radius of circle
        num_points: Number of points to generate
    
    Returns:
        List of (x, y) tuples
    """
    points = []
    for i in range(num_points):
        angle = (2 * math.pi * i) / num_points
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        points.append((x, y))
    return points


def spiral_points(center_x, center_y, start_radius, end_radius, num_points, rotations=3):
    """
    Generate points along a spiral.
    
    Args:
        center_x: X coordinate of center
        center_y: Y coordinate of center
        start_radius: Starting radius
        end_radius: Ending radius
        num_points: Number of points to generate
        rotations: Number of complete rotations
    
    Returns:
        List of (x, y) tuples
    """
    points = []
    for i in range(num_points):
        progress = i / num_points
        angle = progress * rotations * 2 * math.pi
        radius = start_radius + (end_radius - start_radius) * progress
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        points.append((x, y))
    return points


def grid_points(x, y, width, height, cols, rows, jitter=0):
    """
    Generate a grid of points with optional jitter.
    
    Args:
        x: Starting x coordinate
        y: Starting y coordinate
        width: Width of grid
        height: Height of grid
        cols: Number of columns
        rows: Number of rows
        jitter: Random offset amount (0-1)
    
    Returns:
        List of (x, y) tuples
    """
    points = []
    cell_width = width / cols
    cell_height = height / rows
    
    for row in range(rows):
        for col in range(cols):
            px = x + col * cell_width + cell_width / 2
            py = y + row * cell_height + cell_height / 2
            
            if jitter > 0:
                px += random.uniform(-cell_width * jitter, cell_width * jitter)
                py += random.uniform(-cell_height * jitter, cell_height * jitter)
            
            points.append((px, py))
    
    return points


def lerp(start, end, t):
    """Linear interpolation between two values."""
    return start + (end - start) * t


def distance(x1, y1, x2, y2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
