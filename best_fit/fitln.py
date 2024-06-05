import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Sample data points
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 5, 10, 17, 26])  # Example data, replace with your own data

# Log-transform the data
log_x = np.log(x)
log_y = np.log(y)

# Define the power law function
def power_law(x, a, b):
    return a * np.power(x, b)

# Fit the power law function to the log-transformed data
params_power_law, _ = curve_fit(power_law, x, y)

# Define the exponential function
def exponential(x, a, b):
    return a * np.exp(b * x)

# Fit the exponential function to the log-transformed data
params_exponential, _ = curve_fit(exponential, x, y)

# Plot the scatter plot in log-log scale
plt.scatter(log_x, log_y, color='blue', label='Log-Transformed Data')

# Plot the best-fit curve for power law in log-log scale
x_values = np.linspace(min(log_x), max(log_x), 100)
y_values_power_law = power_law(np.exp(x_values), *params_power_law)
plt.plot(x_values, np.log(y_values_power_law), color='red', label='Best-fit curve (Power Law)')

# Plot the best-fit curve for exponential in log-log scale
y_values_exponential = exponential(np.exp(x_values), *params_exponential)
plt.plot(x_values, np.log(y_values_exponential), color='green', label='Best-fit curve (Exponential)')

plt.xlabel('log(X)')
plt.ylabel('log(Y)')
plt.title('Log-Log Plot with Best-fit Curves')
plt.legend()
plt.grid(True)
plt.show()

# Print parameters of best-fit curves
print("Power Law Parameters:", params_power_law)
print("Exponential Parameters:", params_exponential)
