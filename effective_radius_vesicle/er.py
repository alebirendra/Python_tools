## data file formatted as (xyz.dat) : time_step particle_id x y z


import numpy as np
import pandas as pd

def calculate_com(positions):
    """
    Calculate the center of mass for given positions.
    
    Args:
    positions (np.ndarray): Array of shape (n_particles, 3) representing particle positions.
    
    Returns:
    np.ndarray: Center of mass coordinates.
    """
    return np.mean(positions, axis=0)

def calculate_effective_radius(positions, com):
    """
    Calculate the effective radius as the average distance from the center of mass.
    
    Args:
    positions (np.ndarray): Array of shape (n_particles, 3) representing particle positions.
    com (np.ndarray): Center of mass coordinates.
    
    Returns:
    float: Effective radius.
    """
    distances = np.linalg.norm(positions - com, axis=1)
    return np.mean(distances)

# Load data
df = pd.read_csv('xyz.dat', delim_whitespace=True, header=None, names=['time_step', 'particle_id', 'x', 'y', 'z'])

# Unique time steps
time_steps = df['time_step'].unique()
effective_radii = []

for t in time_steps:
    subset = df[df['time_step'] == t]
    positions = subset[['x', 'y', 'z']].values
    
    # Calculate center of mass
    com = calculate_com(positions)
    
    # Calculate effective radius
    effective_radius = calculate_effective_radius(positions, com)
    effective_radii.append(effective_radius)
    
    print(f"Time step {t}: Effective Radius = {effective_radius}")

# Optionally, save results to a file
with open('effective_radii.dat', 'w') as f:
    for t, radius in zip(time_steps, effective_radii):
        f.write(f"{t} {radius}\n")

print("Effective radius calculation complete. Results saved to effective_radii.dat.")
