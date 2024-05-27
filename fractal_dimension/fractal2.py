## Box-Counting Method: This method involves covering the particle coordinates with boxes of varying sizes and counting the number 
## of boxes that contain at least one particle. The relationship between the number of boxes and the box size is used to calculate the fractal dimension.

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def box_counting(data, min_box_size=0.01, max_box_size=0.1, num_box_sizes=10):
    """
    Calculate the fractal dimension using box-counting method.
    """
    box_sizes = np.logspace(np.log10(min_box_size), np.log10(max_box_size), num=num_box_sizes)
    counts = []

    for box_size in box_sizes:
        bins = [np.arange(0, 1+box_size, box_size)] * 3
        H, _ = np.histogramdd(data, bins=bins)
        counts.append(np.sum(H > 0))

    return box_sizes, counts

def fractal_dimension(data, min_box_size=0.01, max_box_size=0.1, num_box_sizes=10):
    box_sizes, counts = box_counting(data, min_box_size, max_box_size, num_box_sizes)
    log_box_sizes = np.log(box_sizes)
    log_counts = np.log(counts)
    
    # Fit linear regression model
    model = LinearRegression().fit(log_box_sizes.reshape(-1, 1), log_counts)
    fractal_dim = -model.coef_[0]

    return fractal_dim

# Load data
df = pd.read_csv('vesicle_data.csv')

# Calculate fractal dimension for each time step
time_steps = df['time_step'].unique()
fractal_dimensions = []

for t in time_steps:
    subset = df[df['time_step'] == t]
    positions = subset[['x', 'y', 'z']].values
    fractal_dim = fractal_dimension(positions)
    fractal_dimensions.append(fractal_dim)
    print(f"Time step {t}: Fractal Dimension = {fractal_dim}")

# Plot fractal dimension over time
plt.plot(time_steps, fractal_dimensions, marker='o')
plt.xlabel('Time Step')
plt.ylabel('Fractal Dimension')
plt.title('Fractal Dimension over Time')
plt.show()
