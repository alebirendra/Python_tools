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
epsilon = 1.0  # LJ potential depth for hydrophilic interaction
sigma = 1.0  # LJ potential distance scale
r_cutoff = 2.5 * sigma  # Cutoff distance for LJ potential

# Initialize particle positions randomly in the box
positions = np.random.rand(num_particles, 3) * box_size

# Initialize particle orientations randomly
orientations = np.random.randn(num_particles, 3)
orientations /= np.linalg.norm(orientations, axis=1).reshape(-1, 1)  # Normalize orientations

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

# Function to compute anisotropic interaction forces
def compute_forces(positions, orientations):
    forces = np.zeros_like(positions)
    torques = np.zeros_like(orientations)
    for i in range(num_particles):
        for j in range(i + 1, num_particles):
            r_vec = positions[i] - positions[j]
            r_vec -= box_size * np.round(r_vec / box_size)  # Apply periodic boundary conditions
            r = np.linalg.norm(r_vec)
            if r < r_cutoff:
                # Compute orientation-dependent interaction
                dot_product = np.dot(orientations[i], orientations[j])
                if dot_product > 0:  # Attractive interaction if hydrophilic patches face each other
                    f = lennard_jones_force(r) * r_vec / r
                    forces[i] += f
                    forces[j] -= f

                    # Calculate torques for orientation adjustment
                    torque_i = np.cross(orientations[i], f)
                    torque_j = np.cross(orientations[j], -f)
                    torques[i] += torque_i
                    torques[j] += torque_j
    return forces, torques

# Open file for output
with open('xyz.dat', 'w') as f:
    f.write("time_step particle_id x y z orientation_x orientation_y orientation_z\n")

    # Main simulation loop
    for step in range(total_steps):
        # Compute forces and torques
        forces, torques = compute_forces(positions, orientations)
        
        # Update positions using Brownian dynamics
        random_forces = np.sqrt(2 * kB * temperature * gamma / dt) * np.random.randn(num_particles, 3)
        positions += (forces / gamma + random_forces) * dt
        
        # Update orientations
        random_torques = np.sqrt(2 * kB * temperature * gamma / dt) * np.random.randn(num_particles, 3)
        orientations += (torques / gamma + random_torques) * dt
        orientations /= np.linalg.norm(orientations, axis=1).reshape(-1, 1)  # Normalize orientations
        
        # Apply periodic boundary conditions
        positions %= box_size

        # Write positions and orientations to file
        for i in range(num_particles):
            f.write(f"{step} {i+1} {positions[i,0]:.6f} {positions[i,1]:.6f} {positions[i,2]:.6f} "
                    f"{orientations[i,0]:.6f} {orientations[i,1]:.6f} {orientations[i,2]:.6f}\n")
        
        # Output positions for visualization at intervals (optional)
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
