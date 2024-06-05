import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
x = np.linspace(1, 100, 100)
y = np.linspace(1, 100, 100)

# Add curvature to the data
y = np.power(x, 0.5)

# Plot the scatter plot in log-log scale
plt.scatter(np.log(x), np.log(y), color='blue', label='Log-Transformed Data')

# Plot the best-fit line (linear regression)
coefficients = np.polyfit(np.log(x), np.log(y), 1)
line = coefficients[0] * np.log(x) + coefficients[1]
plt.plot(np.log(x), line, color='red', label='Best-fit Line')

plt.xlabel('log(X)')
plt.ylabel('log(Y)')
plt.title('Log-Log Plot with Curved Behavior')
plt.legend()
plt.grid(True)
plt.show()

# Print the coefficients of the best-fit line
print("Best-fit Line Coefficients:", coefficients)
