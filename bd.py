import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
num_particles = 100
box_size = 10.0
dt = 0.001
total_steps = 10000
temperature = 1.0
gamma = 1.0  # friction coefficient
kB = 1.0  # Boltzmann constant
epsilon = 1.0  # LJ potential depth
sigma = 1.0  # LJ potential distance scale
r_cutoff = 2.5 * sigma  # Cutoff distance for LJ potential

# Initialize particle positions randomly in the box
positions = np.random.rand(num_particles, 3) * box_size

# Initialize velocities to zero
velocities = np.zeros((num_particles, 3))

# Define the Lennard-Jones potential and force
def lennard_jones_potential(r):
    sr6 = (sigma / r)**6
    sr12 = sr6**2
    return 4 * epsilon * (sr12 - sr6)

def lennard_jones_force(r):
    sr6 = (sigma / r)**6
    sr12 = sr6**2
    return 24 * epsilon * (2 * sr12 - sr6) / r

# Function to compute forces
def compute_forces(positions):
    forces = np.zeros_like(positions)
    for i in range(num_particles):
        for j in range(i + 1, num_particles):
            r_vec = positions[i] - positions[j]
            r_vec -= box_size * np.round(r_vec / box_size)  # Apply periodic boundary conditions
            r = np.linalg.norm(r_vec)
            if r < r_cutoff:
                f = lennard_jones_force(r) * r_vec / r
                forces[i] += f
                forces[j] -= f
    return forces

# Main simulation loop
for step in range(total_steps):
    # Compute forces
    forces = compute_forces(positions)
    
    # Update positions using Brownian dynamics
    random_forces = np.sqrt(2 * kB * temperature * gamma / dt) * np.random.randn(num_particles, 3)
    positions += (forces / gamma + random_forces) * dt
    
    # Apply periodic boundary conditions
    positions %= box_size

    # Output positions for visualization at intervals
    if step % 1000 == 0:
        plt.figure(figsize=(6, 6))
        plt.scatter(positions[:, 0], positions[:, 1], s=10)
        plt.xlim(0, box_size)
        plt.ylim(0, box_size)
        plt.title(f"Step {step}")
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

print("Simulation complete.")
