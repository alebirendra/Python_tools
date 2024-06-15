pip install matplotlib-ternary


import matplotlib.pyplot as plt
import ternary

# Define the ternary plot scale
scale = 100

# Create a figure and ternary axis
fig, ax = plt.subplots(figsize=(10, 8))
ax = ternary.TernaryAxesSubplot(ax=ax, scale=scale)
ax.boundary(linewidth=2.0)
ax.gridlines(color="black", multiple=10, linewidth=0.5)
ax.set_title("Ternary Phase Diagram of O-Zn-Mg", fontsize=20)

# Label the corners
ax.left_axis_label("Oxygen (O)", fontsize=15)
ax.right_axis_label("Zinc (Zn)", fontsize=15)
ax.bottom_axis_label("Magnesium (Mg)", fontsize=15)

# Example data points
# The data points should be in the format: (Mg, Zn, O)
data = [
    (20, 30, 50),
    (30, 30, 40),
    (10, 20, 70),
    (40, 20, 40),
    (25, 50, 25)
]

# Plot the data points
ax.scatter(data, marker='o', color='red', label='Data Points')

# Set ticks and remove default axis
ax.ticks(axis='lbr', multiple=10, linewidth=1)
ax.clear_matplotlib_ticks()

# Add legend
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()
