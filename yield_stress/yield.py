import numpy as np
import matplotlib.pyplot as plt

# Hypothetical data
shear_rates = np.linspace(0.1, 100, 50)  # range of shear rates in s^-1
vesicle_radius = 1e-6  # characteristic length scale in meters
diffusion_coefficient = 1e-12  # diffusion coefficient in m^2/s

# Calculate Péclet number
peclet_numbers = (shear_rates * vesicle_radius**2) / diffusion_coefficient

# Hypothetical yield stress data corresponding to each shear rate
yield_stress = 0.1 * np.log(peclet_numbers + 1)  # example function

# Plot yield stress vs. Péclet number
plt.figure(figsize=(8, 6))
plt.plot(peclet_numbers, yield_stress, marker='o', linestyle='-')
plt.xlabel('Péclet Number (Pe)')
plt.ylabel('Yield Stress (Pa)')
plt.title('Yield Stress as a Function of Péclet Number')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.show()
