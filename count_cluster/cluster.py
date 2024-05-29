%%time

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# Read the data from the file
data = pd.read_csv('pos.dat', sep='\s+', names=["time_step", "particle_id", "x", "y", "z"])
t_step = data['time_step'].unique()

# Parameters
num_particles = 26  # Number of particles in a vesicle
max_time_step = 20000  # Number of time steps in the simulation
eps = 2.2  # Maximum distance between two samples for one to be considered as in the neighborhood of the other
min_samples = 1  # The number of samples (or total weight) in a neighborhood for a point to be considered as a core point

# Initialize a list to store the number of clusters at each time step
num_clusters = []

# Loop through each time step
for t in range(1, max_time_step + 1):
    # Extract the positions at the current time step
    time_step_data = data[data['time_step'] == t_step[t]][["x", "y", "z"]].values
  #  print(time_step_data)
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

# save results to a file
with open('nc.dat', 'w') as f:
    for t, nc in zip(range(len(num_clusters)), num_clusters):
        f.write(f"{t} {nc}\n")


# Plot the number of clusters as a function of time step
plt.figure(figsize=(10, 6))
plt.plot(range(1, max_time_step + 1), num_clusters, marker='o', linestyle='-')
plt.xscale('log')
plt.yscale('log')
plt.ylim([1,100])
plt.xlabel('Time Step')
plt.ylabel('Number of Clusters')
plt.title('Number of Clusters as a Function of Time Step')
plt.grid(True)
plt.show()
