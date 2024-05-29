from scipy.interpolate import UnivariateSpline
data = pd.read_csv('nc.dat', sep='\s+', names=["time_step", "nc" ])

# Spline fitting
spline = UnivariateSpline(data['time_step'], data['nc'])
spline.set_smoothing_factor(10)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(data['time_step'], data['nc'], label='Original Data', alpha=0.5)
plt.plot(data['time_step'], spline(data['time_step']), label='Spline Fit', color='purple')
plt.legend()
plt.xlabel('time_step')
plt.ylabel('nc')
plt.title('Spline Fitting')
plt.show()
