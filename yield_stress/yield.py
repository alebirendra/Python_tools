import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('vesicle_data.csv')

# Parameters
num_particles = 18
time_steps = data['time_step'].nunique()

# Reshape data into 3D array: (time_steps, num_particles, 3)
positions = data[['x', 'y', 'z']].values.reshape(time_steps, num_particles, 3)

# Calculate strain rate
strain_rate = []
for t in range(1, time_steps):
    displacement = positions[t] - positions[t-1]
    displacement_magnitude = np.linalg.norm(displacement, axis=1)
    avg_displacement = np.mean(displacement_magnitude)
    strain_rate.append(avg_displacement)

# Apply hypothetical stresses for demonstration
stresses = np.linspace(0.1, 10, len(strain_rate))

# Plot Stress vs. Strain Rate
plt.plot(stresses, strain_rate, marker='o')
plt.xlabel('Shear Stress')
plt.ylabel('Strain Rate')
plt.title('Stress vs. Strain Rate')
plt.show()

# Identify yield stress as the point where strain rate begins to increase significantly
yield_stress = stresses[np.argmax(np.gradient(strain_rate))]
print(f'Yield Stress: {yield_stress} Pa')
