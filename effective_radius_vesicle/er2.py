import pandas as pd
import numpy as np

def calculate_effective_radius(data):
    # Group by time_step
    grouped = data.groupby('time_step')

    effective_radii = []

    for time_step, group in grouped:
        # Calculate the center of mass
        center_of_mass = group[['x', 'y', 'z']].mean().values
        
        # Calculate the radius of gyration
        squared_distances = np.sum((group[['x', 'y', 'z']] - center_of_mass) ** 2, axis=1)
        radius_of_gyration = np.sqrt(np.mean(squared_distances))
        
        effective_radii.append((time_step, radius_of_gyration))
    
    return effective_radii

# Read the data
data = pd.read_csv('xyz.dat', sep='\s+', names=['time_step', 'particle_id', 'x', 'y', 'z'])

# Calculate the effective radius
effective_radii = calculate_effective_radius(data)

# Print the results
for time_step, radius in effective_radii:
    print(f"Time Step: {time_step}, Effective Radius: {radius:.4f}")
