# Manim Animations for Week 2: Linear Regression

This folder contains Manim animation scripts and generated videos for the linear regression lecture.

## Setup

1. Install Manim Community Edition:
```bash
pip install manim
```

2. Generate animations:
```bash
# Generate a specific scene in 1080p quality
manim -pqh gradient_descent.py GradientDescentAnimation

# Generate all scenes in medium quality (faster)
manim -pqm gradient_descent.py

# Generate for presentation (720p, good balance)
manim -pql gradient_descent.py GradientDescentAnimation
```

## Animation Files

- `gradient_descent.py` - Visualization of gradient descent optimization
- `normal_equations.py` - Geometric interpretation of least squares
- `residuals.py` - Visualizing residuals and RSS minimization

## Video Output

Videos are generated in `media/videos/[script_name]/[quality]/`

For embedding in Quarto presentations, use relative paths:
```markdown
![](animations/media/videos/gradient_descent/1080p60/GradientDescentAnimation.mp4)
```

## Quality Settings

- `-pql`: 480p (low quality, fast rendering)
- `-pqm`: 720p (medium quality)
- `-pqh`: 1080p (high quality)
- `-pqk`: 4K (ultra high quality, slow)

## Tips

- Use `--save_last_frame` to generate a thumbnail
- Use `-s` to save the last frame only (for testing)
- Use `-p` to preview after rendering
