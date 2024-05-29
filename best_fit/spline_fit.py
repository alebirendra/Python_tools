from scipy.interpolate import UnivariateSpline

# Spline fitting
spline = UnivariateSpline(data['x'], data['y'])
spline.set_smoothing_factor(1)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(data['x'], data['y'], label='Original Data', alpha=0.5)
plt.plot(data['x'], spline(data['x']), label='Spline Fit', color='purple')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Spline Fitting')
plt.show()
