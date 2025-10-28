# vibe-lab 🎨

Experimental creative-coding sketches built with AI assistance. A Python-based sandbox for generating visual art and motion sketches using Pygame.

## Features

- 🎨 **Generative Art**: Create unique visual patterns with algorithmic designs
- 🌊 **Motion Sketches**: Animated patterns with flowing particles and waves
- 🎨 **Color Harmony**: Built-in color palette generation for aesthetically pleasing results
- 🔧 **Utility Library**: Reusable modules for colors and geometric patterns
- 💡 **Interactive**: Real-time manipulation with keyboard controls

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Mark5484/vibe-lab.git
cd vibe-lab
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

### Run the interactive menu:
```bash
python main.py
```

### Run individual examples:

**Generative Circles** - Static art with overlapping transparent circles:
```bash
python examples/circles.py
```
- Press `SPACE` to generate new art
- Press `Q` to quit

**Animated Spiral** - Flowing particles in spiral patterns:
```bash
python examples/spiral_motion.py
```
- Press `SPACE` to regenerate with new colors
- Press `Q` to quit

**Grid Waves** - Dynamic wave patterns on a grid:
```bash
python examples/grid_waves.py
```
- Press `SPACE` to toggle animation
- Press `R` to randomize pattern
- Press `Q` to quit

## Project Structure

```
vibe-lab/
├── main.py              # Interactive menu to run examples
├── requirements.txt     # Python dependencies
├── src/                 # Core utility modules
│   ├── __init__.py
│   ├── colors.py       # Color utilities and palette generation
│   └── geometry.py     # Geometric shapes and point generation
└── examples/            # Example sketches
    ├── circles.py      # Generative circles
    ├── spiral_motion.py # Animated spiral
    └── grid_waves.py   # Grid wave patterns
```

## Core Utilities

### Colors Module (`src/colors.py`)

- `generate_palette(base_hue, count, saturation, value)` - Generate harmonious color palettes
- `interpolate_color(color1, color2, factor)` - Smooth color transitions
- `hsv_to_rgb(h, s, v)` - Color space conversion
- `random_color()` - Random color generation

### Geometry Module (`src/geometry.py`)

- `circle_points(x, y, radius, num_points)` - Points around a circle
- `spiral_points(x, y, start_r, end_r, points, rotations)` - Spiral path points
- `grid_points(x, y, width, height, cols, rows, jitter)` - Grid layout with optional randomness
- `lerp(start, end, t)` - Linear interpolation
- `distance(x1, y1, x2, y2)` - Distance calculation

## Creating Your Own Sketches

1. Create a new Python file in the `examples/` directory
2. Import utilities from `src/`:
```python
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.colors import generate_palette
from src.geometry import circle_points
```

3. Use Pygame to create your visual:
```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
# Your creative code here!
```

## AI-Assisted Features (Optional)

To enable AI-assisted generative art features, uncomment the AI libraries in `requirements.txt`:
```txt
openai==1.12.0
anthropic==0.18.1
```

Then install them:
```bash
pip install -r requirements.txt
```

## Tips for Creative Coding

- Experiment with different color palettes by changing the `base_hue` parameter
- Combine multiple geometric patterns for complex designs
- Use time-based animations for organic motion
- Save your favorite outputs using `pygame.image.save()`
- Try varying opacity/alpha values for layered effects

## Contributing

Feel free to add your own sketches and utilities! This is an experimental sandbox for creative exploration.

## License

MIT License - Feel free to use and modify for your own creative projects!
