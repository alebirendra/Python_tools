import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# Read the data from the file
data = pd.read_csv('xyz.dat', delim_whitespace=True, names=["time_step", "particle_id", "x", "y", "z"])

# Parameters
num_particles = 18  # Number of particles in a vesicle
max_time_step = 1000  # Number of time steps in the simulation
eps = 0.1  # Maximum distance between two samples for one to be considered as in the neighborhood of the other
min_samples = 2  # The number of samples (or total weight) in a neighborhood for a point to be considered as a core point

# Initialize a list to store the number of clusters at each time step
num_clusters = []

# Loop through each time step
for t in range(1, max_time_step + 1):
    # Extract the positions at the current time step
    time_step_data = data[data['time_step'] == t][["x", "y", "z"]].values
    
    # Check if the number of particles at the current time step matches the expected number
    if len(time_step_data) != num_particles:
        print(f"Warning: Missing or extra data for time step {t}. Expected {num_particles} particles, got {len(time_step_data)}.")
        num_clusters.append(np.nan)  # Append NaN for inconsistent data
        continue

    # Perform DBSCAN clustering
    clustering = DBSCAN(eps=eps, min_samples=min_samples).fit(time_step_data)

    # Count the number of clusters (excluding noise)
    labels = clustering.labels_
    num_clusters.append(len(set(labels)) - (1 if -1 in labels else 0))

# Handle NaN values (e.g., interpolate or ignore in plotting)
num_clusters = pd.Series(num_clusters).interpolate().tolist()

# Plot the number of clusters as a function of time step
plt.figure(figsize=(10, 6))
plt.plot(range(1, max_time_step + 1), num_clusters, marker='o', linestyle='-')
plt.xlabel('Time Step')
plt.ylabel('Number of Clusters')
plt.title('Number of Clusters as a Function of Time Step')
plt.grid(True)
plt.show()
