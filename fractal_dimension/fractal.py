import numpy as np

def box_counting_fractal_dimension(positions, box_sizes):
    """
    Calculate the fractal dimension using the box-counting method.

    Args:
    positions (np.ndarray): An array of shape (N, 3) containing the coordinates.
    box_sizes (np.ndarray): An array of box sizes to use for the box-counting method.

    Returns:
    float: The fractal dimension.
    """
    num_boxes = []
    for size in box_sizes:
        count = 0
        for x in np.arange(0, 1, size):
            for y in np.arange(0, 1, size):
                for z in np.arange(0, 1, size):
                    if np.any((positions >= [x, y, z]) & (positions < [x+size, y+size, z+size]), axis=1).any():
                        count += 1
        num_boxes.append(count)
    return np.polyfit(np.log(1/box_sizes), np.log(num_boxes), 1)[0]

def calculate_fractal_dimensions_over_time(data, time_steps, box_sizes):
    """
    Calculate the fractal dimensions at different time steps.

    Args:
    data (np.ndarray): An array of shape (time_steps, num_particles, 3) containing the coordinates.
    time_steps (int): Number of time steps.
    box_sizes (np.ndarray): An array of box sizes to use for the box-counting method.

    Returns:
    np.ndarray: Fractal dimensions at each time step.
    """
    fractal_dimensions = []
    for t in range(time_steps):
        positions = data[t]
        fractal_dim = box_counting_fractal_dimension(positions, box_sizes)
        fractal_dimensions.append(fractal_dim)
    return np.array(fractal_dimensions)

# Example usage
# Assume 'data' is a numpy array of shape (time_steps, 26, 3) containing the coordinates of the vesicle particles at each time step.
# Here we generate random data for demonstration. Replace with actual data loading.
time_steps = 10
num_particles = 26
data = np.random.rand(time_steps, num_particles, 3)  # Replace with actual data
box_sizes = np.logspace(-3, 0, num=10)  # Example range of box sizes

fractal_dimensions = calculate_fractal_dimensions_over_time(data, time_steps, box_sizes)

for t, fd in enumerate(fractal_dimensions):
    print(f"Time step {t}: Fractal Dimension = {fd:.4f}")
