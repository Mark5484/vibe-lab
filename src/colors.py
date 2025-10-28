"""
Color utilities for generative art
"""
import colorsys
import random


def interpolate_color(color1, color2, factor):
    """
    Interpolate between two RGB colors.
    
    Args:
        color1: Tuple of (r, g, b) values (0-255)
        color2: Tuple of (r, g, b) values (0-255)
        factor: Float between 0 and 1 (0 = color1, 1 = color2)
    
    Returns:
        Tuple of (r, g, b) interpolated color
    """
    r = int(color1[0] + (color2[0] - color1[0]) * factor)
    g = int(color1[1] + (color2[1] - color1[1]) * factor)
    b = int(color1[2] + (color2[2] - color1[2]) * factor)
    return (r, g, b)


def hsv_to_rgb(h, s, v):
    """
    Convert HSV color to RGB.
    
    Args:
        h: Hue (0-360)
        s: Saturation (0-1)
        v: Value (0-1)
    
    Returns:
        Tuple of (r, g, b) values (0-255)
    """
    r, g, b = colorsys.hsv_to_rgb(h / 360.0, s, v)
    return (int(r * 255), int(g * 255), int(b * 255))


def generate_palette(base_hue=None, count=5, saturation=0.7, value=0.9):
    """
    Generate a harmonious color palette.
    
    Args:
        base_hue: Starting hue (0-360), or None for random
        count: Number of colors to generate
        saturation: Saturation value (0-1)
        value: Value/brightness (0-1)
    
    Returns:
        List of RGB color tuples
    """
    if base_hue is None:
        base_hue = random.randint(0, 360)
    
    palette = []
    for i in range(count):
        hue = (base_hue + (i * 360 / count)) % 360
        palette.append(hsv_to_rgb(hue, saturation, value))
    
    return palette


def random_color():
    """Generate a random RGB color."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
