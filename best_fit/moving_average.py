import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data
data = pd.read_csv('nc.dat', sep='\s+', names=["time_step", "nc" ])

# Moving average
window_size = 25
data['y_smooth'] = data['nc'].rolling(window=window_size, center=True).mean()

# Plotting
plt.figure(figsize=(10, 6))
plt.xscale('log')
plt.yscale('log')
plt.ylim([1,100])
plt.plot(data['time_step'], data['nc'], label='Original Data', alpha=0.5)
plt.plot(data['time_step'], data['y_smooth'], label='Smoothed Data (Moving Average)', color='red')
plt.legend()
plt.xlabel('time_step')
plt.ylabel('nc')
plt.title('Moving Average Smoothing')
plt.show()
