import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

fig, ax = plt.subplots(figsize=(5, 2))
ax.axis("off")

# Traditional Programming
ax.text(
    0.05,
    0.8,
    "Input\n(Data)",
    ha="center",
    va="center",
    fontsize=12,
    bbox=dict(boxstyle="round", facecolor="#e0e0e0"),
)
ax.text(0.25, 0.8, "+", ha="center", va="center", fontsize=14)
ax.text(
    0.4,
    0.8,
    "Program\n(Rules)",
    ha="center",
    va="center",
    fontsize=12,
    bbox=dict(boxstyle="round", facecolor="#e0e0e0"),
)
ax.text(0.55, 0.8, "\u2192", ha="center", va="center", fontsize=16)
ax.text(
    0.7,
    0.8,
    "Output\n(Prediction)",
    ha="center",
    va="center",
    fontsize=12,
    bbox=dict(boxstyle="round", facecolor="#b3e5fc"),
)
ax.text(
    0.5,
    0.95,
    "Traditional Programming",
    ha="center",
    va="center",
    fontsize=11,
    fontweight="bold",
)

# Machine Learning
ax.text(
    0.05,
    0.3,
    "Input\n(Data)",
    ha="center",
    va="center",
    fontsize=12,
    bbox=dict(boxstyle="round", facecolor="#e0e0e0"),
)
ax.text(0.25, 0.3, "+", ha="center", va="center", fontsize=14)
ax.text(
    0.4,
    0.3,
    "Output\n(Labels)",
    ha="center",
    va="center",
    fontsize=12,
    bbox=dict(boxstyle="round", facecolor="#ffe082"),
)
ax.text(0.55, 0.3, "\u2192", ha="center", va="center", fontsize=16)
ax.text(
    0.7,
    0.3,
    "Program\n(Model)",
    ha="center",
    va="center",
    fontsize=12,
    bbox=dict(boxstyle="round", facecolor="#c8e6c9"),
)
ax.text(
    0.5,
    0.45,
    "Machine Learning",
    ha="center",
    va="center",
    fontsize=11,
    fontweight="bold",
)

plt.tight_layout()
plt.savefig("images/ai_ml_diagram.png", dpi=150, bbox_inches="tight")
plt.close()
