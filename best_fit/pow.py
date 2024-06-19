import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample data (replace this with your actual data)
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([10, 5, 2, 1.5, 1.2, 1, 0.9, 0.8, 0.7, 0.6])

# Take the logarithm of x and y values
log_x = np.log(x)
log_y = np.log(y)

# Reshape for sklearn
log_x = log_x.reshape(-1, 1)

# Perform linear regression on log-log data
model = LinearRegression()
model.fit(log_x, log_y)

# Extract slope (n) and intercept (log(k))
n = model.coef_[0]
log_k = model.intercept_

# Transform back to original scale
k = np.exp(log_k)

# Print the results
print(f"Best fit equation: y = {k:.3f} * x^{n:.3f}")

# Generate the best-fit line
x_fit = np.linspace(min(x), max(x), 100)
y_fit = k * x_fit**n

# Plot the original data and the best-fit line
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='Data')
plt.plot(x_fit, y_fit, color='red', label=f'Best fit: $y = {k:.3f} \cdot x^{n:.3f}$')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('x (log scale)')
plt.ylabel('y (log scale)')
plt.title('Log-Log Scale Hyperbolic Fit')
plt.legend()
plt.grid(True)
plt.show()
