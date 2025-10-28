"""
Vibe Lab - Creative Coding Sandbox
Main entry point for running examples.
"""
import sys
import os


def print_menu():
    """Print the main menu."""
    print("\n" + "="*60)
    print("  VIBE LAB - Creative Coding Sandbox")
    print("="*60)
    print("\nAvailable sketches:")
    print("  1. Circles      - Generative art with overlapping circles")
    print("  2. Spiral       - Animated spiral with flowing particles")
    print("  3. Grid Waves   - Dynamic wave patterns on a grid")
    print("\n  Q. Quit")
    print("="*60)


def run_example(choice):
    """Run the selected example."""
    examples_dir = os.path.join(os.path.dirname(__file__), 'examples')
    
    examples = {
        '1': 'circles.py',
        '2': 'spiral_motion.py',
        '3': 'grid_waves.py',
    }
    
    if choice in examples:
        example_path = os.path.join(examples_dir, examples[choice])
        print(f"\nLaunching {examples[choice]}...")
        print("-" * 60)
        
        # Run the example in a subprocess to allow returning to menu
        import subprocess
        subprocess.run([sys.executable, example_path])
        
        return True
    return False


def main():
    """Main function."""
    while True:
        print_menu()
        choice = input("\nEnter your choice: ").strip().lower()
        
        if choice == 'q':
            print("\nThanks for using Vibe Lab! Keep creating! 🎨")
            break
        elif run_example(choice):
            continue
        else:
            print(f"\nInvalid choice: {choice}")


if __name__ == "__main__":
    main()
