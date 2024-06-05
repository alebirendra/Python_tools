import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
x = np.linspace(1, 100, 100)
y = np.linspace(1, 100, 100)

# Add noise to make the curve deviate from the diagonal
noise = np.random.normal(scale=0.1, size=len(x))
y = y - noise

# Plot the scatter plot in log-log scale
plt.scatter(np.log(x), np.log(y), color='blue', label='Log-Transformed Data')

# Plot the diagonal line representing the behavior
plt.plot(np.log(x), np.log(x), color='red', label='Diagonal Line (Slope=1)')

plt.xlabel('log(X)')
plt.ylabel('log(Y)')
plt.title('Log-Log Plot with Curving Line towards Origin')
plt.legend()
plt.grid(True)
plt.show()
