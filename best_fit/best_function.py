import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Sample data points
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 5, 10, 17, 26])  # Example data, replace with your own data

# Define candidate models
def linear_model(x, a, b):
    return a * x + b

def quadratic_model(x, a, b, c):
    return a * x**2 + b * x + c

def exponential_model(x, a, b):
    return a * np.exp(b * x)

# Fit candidate models to the data
popt_linear, _ = curve_fit(linear_model, x, y)
popt_quadratic, _ = curve_fit(quadratic_model, x, y)
popt_exponential, _ = curve_fit(exponential_model, x, y)

# Calculate goodness of fit measures (R-squared)
def r_squared(y, y_pred):
    residual = y - y_pred
    rss = np.sum(residual**2)
    tss = np.sum((y - np.mean(y))**2)
    return 1 - (rss / tss)

y_linear = linear_model(x, *popt_linear)
y_quadratic = quadratic_model(x, *popt_quadratic)
y_exponential = exponential_model(x, *popt_exponential)

r_squared_linear = r_squared(y, y_linear)
r_squared_quadratic = r_squared(y, y_quadratic)
r_squared_exponential = r_squared(y, y_exponential)

# Select the best model based on R-squared
best_model = max([(r_squared_linear, 'Linear'), (r_squared_quadratic, 'Quadratic'), (r_squared_exponential, 'Exponential')], key=lambda x: x[0])
print("Best-fit model:", best_model[1])

# Plot the scatter plot
plt.scatter(x, y, color='blue', label='Data')

# Plot the best-fit curve
if best_model[1] == 'Linear':
    plt.plot(x, linear_model(x, *popt_linear), color='red', label='Best-fit curve (Linear)')
elif best_model[1] == 'Quadratic':
    plt.plot(x, quadratic_model(x, *popt_quadratic), color='red', label='Best-fit curve (Quadratic)')
else:
    plt.plot(x, exponential_model(x, *popt_exponential), color='red', label='Best-fit curve (Exponential)')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot with Best-fit Curve')
plt.legend()
plt.grid(True)
plt.show()
