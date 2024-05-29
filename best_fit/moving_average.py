import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data
data = pd.DataFrame({'x': np.linspace(0, 10, 100), 'y': np.sin(np.linspace(0, 10, 100)) + np.random.normal(scale=0.5, size=100)})

# Moving average
window_size = 5
data['y_smooth'] = data['y'].rolling(window=window_size, center=True).mean()

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(data['x'], data['y'], label='Original Data', alpha=0.5)
plt.plot(data['x'], data['y_smooth'], label='Smoothed Data (Moving Average)', color='red')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Moving Average Smoothing')
plt.show()
