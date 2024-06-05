import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Sample data points
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 5, 10, 17, 26])  # Example data, replace with your own data

# Define the power law function
def power_law(x, a, b):
    return a * np.power(x, b)

# Fit the power law function to the data
params, covariance = curve_fit(power_law, x, y)

# Extract parameters
a, b = params

# Formulate equation
equation = f'y = {a:.2f} * x^{b:.2f}'

print("Equation of best-fit curve:", equation)

# Plot the scatter plot
plt.scatter(x, y, color='blue', label='Data')

# Plot the best-fit curve
x_values = np.linspace(min(x), max(x), 100)
y_values = power_law(x_values, a, b)
plt.plot(x_values, y_values, color='red', label='Best-fit curve')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot with Best-fit Curve')
plt.legend()
plt.grid(True)
plt.show()
