# AERO 689 Quarto Presentation Theme Guide

## Overview

This directory contains a custom Quarto theme for AERO 689 presentations, designed with an aerospace engineering aesthetic featuring professional styling, code highlighting, and specialized content blocks.

## Theme Files

- **`_quarto.yml`**: Main configuration file with default settings for all presentations
- **`aero689-theme.scss`**: Custom SCSS theme with aerospace-inspired color palette
- **`aero689-custom.css`**: Additional CSS utilities for special content blocks

## Color Palette

```scss
Navy Dark:      #0A1628  // Code backgrounds, dark accents
Navy Primary:   #1A2F4F  // Headings, primary text
Navy Light:     #2D4A6F  // Secondary headings
Blue Accent:    #2E7BB4  // Links, emphasis
Blue Bright:    #4A9FD8  // Hover states, highlights
Sky Blue:       #7CB9E8  // Light accents
Orange Accent:  #E87722  // Warnings, safety-critical
Gold Accent:    #C5912E  // Key equations, takeaways
```

## Creating a Presentation

### Basic Quarto Markdown Structure

Create a `.qmd` file with this header:

```yaml
---
title: "Week X: Topic Name"
subtitle: "AERO 689: Introduction to Machine Learning for Aerospace Engineers"
author: "Dr. Raktim Bhattacharya"
institute: "Texas A&M University - Aerospace Engineering"
date: "January 2026"
format:
  revealjs:
    slide-number: true
    chalkboard: true
---
```

### Slide Separators

```markdown
## New Slide Title

Content here...

---

## Another Slide

More content...
```

## Custom Content Blocks

### Highlight Box
```markdown
::: {.highlight-box}
Important concept or definition that needs emphasis
:::
```

### Safety-Critical Warning
```markdown
::: {.safety-critical}
This algorithm makes life-or-death decisions in flight control systems.
:::
```

### ML Concept Box
```markdown
::: {.ml-concept}
**Supervised Learning**: Learning from labeled training data where inputs are mapped to known outputs.
:::
```

### Key Takeaway
```markdown
::: {.key-takeaway}
Always validate ML models with physics-based constraints in aerospace applications.
:::
```

### Interactive Question
```markdown
::: {.interactive-question}
What sensors would you use to detect a stall condition?
:::
```

### Learning Objectives
```markdown
[Learning Objective 1]{.learning-objective}
[Learning Objective 2]{.learning-objective}
[Learning Objective 3]{.learning-objective}
```

### Aerospace Formula Display
```markdown
::: {.aero-formula}
$$C_D = C_{D_0} + K \cdot C_L^2$$
:::
```

## Code Blocks

### Python with Line Numbers
````markdown
```{python}
#| echo: true
#| code-line-numbers: "|2|4-6"

import numpy as np

def drag_coefficient(cl, cd0=0.02, k=0.05):
    """Calculate drag coefficient from lift coefficient"""
    return cd0 + k * cl**2
```
````

### Code with Execution
````markdown
```{python}
#| echo: true
#| output: true

import matplotlib.pyplot as plt
import numpy as np

alpha = np.linspace(-5, 20, 100)
cl = 0.1 * alpha
cd = 0.02 + 0.05 * cl**2

plt.plot(alpha, cl/cd)
plt.xlabel('Angle of Attack (degrees)')
plt.ylabel('Lift-to-Drag Ratio')
plt.title('Aerodynamic Efficiency')
plt.show()
```
````

## Layout Helpers

### Two-Column Layout
```markdown
::: {.columns}
::: {.column width="50%"}
**Left Column**

- Point 1
- Point 2
:::

::: {.column width="50%"}
**Right Column**

- Point A
- Point B
:::
:::
```

### Grid Layouts
```markdown
::: {.grid-2}
<div class="card">
  <div class="card-title">Card 1</div>
  Content here
</div>

<div class="card">
  <div class="card-title">Card 2</div>
  Content here
</div>
:::
```

## Statistics Display

```markdown
::: {.stat-display}
<div class="stat-number">346</div>
<div class="stat-label">Lives Lost</div>
:::
```

## Badges

```markdown
[Python]{.badge .badge-primary}
[Verified]{.badge .badge-success}
[Warning]{.badge .badge-warning}
[Info]{.badge .badge-info}
```

## Advanced Features

### Fragments (Incremental Reveals)
```markdown
::: {.fragment}
This appears first
:::

::: {.fragment}
This appears second
:::

::: {.fragment .highlight-current-blue}
This appears third and highlights when current
:::
```

### Speaker Notes
```markdown
## Slide Content

Visible content here

::: {.notes}
These notes are only visible in speaker view.
Remind students about the homework deadline.
:::
```

### Chalkboard
The chalkboard feature is enabled by default. Press 'c' to toggle drawing mode during presentation.

## Rendering Presentations

### Command Line
```bash
# Render single presentation
quarto render week01_presentation.qmd

# Render all presentations in directory
quarto render

# Live preview with auto-reload
quarto preview week01_presentation.qmd
```

### VS Code
1. Install the Quarto extension
2. Open a `.qmd` file
3. Click "Preview" button or use Cmd/Ctrl+Shift+K

## Export Options

### PDF Export
```bash
quarto render week01_presentation.qmd --to pdf
```

### PowerPoint Export
```bash
quarto render week01_presentation.qmd --to pptx
```

## Keyboard Shortcuts (Presentation Mode)

- **Arrow Keys**: Navigate slides
- **f**: Fullscreen
- **s**: Speaker view
- **o**: Overview mode
- **c**: Toggle chalkboard
- **Esc**: Exit fullscreen/overview
- **?**: Show help

## Best Practices

1. **One Concept Per Slide**: Keep slides focused and uncluttered
2. **Visual Hierarchy**: Use headings (##, ###) consistently
3. **Code Blocks**: Keep to 15-20 lines max per slide
4. **Animations**: Use fragments sparingly for emphasis
5. **Images**: Use high-resolution images, preferably SVG for diagrams
6. **Accessibility**: Ensure sufficient color contrast
7. **Testing**: Preview on different screen sizes

## Examples

See `week01_introduction_motivation/week01_presentation.qmd` for a complete example using all theme features.

## Troubleshooting

### Theme Not Applied
- Ensure `_quarto.yml` is in the presentations directory
- Check that SCSS file names match exactly

### Code Not Highlighting
- Verify Python/R is installed
- Check code block syntax (` ```{python}`)

### Math Not Rendering
- Ensure MathJax is enabled in `_quarto.yml`
- Use `$$` for display math, `$` for inline

## Resources

- [Quarto Presentations Guide](https://quarto.org/docs/presentations/)
- [Reveal.js Documentation](https://revealjs.com/)
- [Quarto SCSS Theming](https://quarto.org/docs/output-formats/html-themes.html)
