from numpy.polynomial.polynomial import Polynomial

# Polynomial fitting
degree = 3
coefs = Polynomial.fit(data['x'], data['y'], degree).convert().coef

# Generate polynomial function
poly = np.poly1d(coefs[::-1])

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(data['x'], data['y'], label='Original Data', alpha=0.5)
plt.plot(data['x'], poly(data['x']), label=f'Polynomial Fit (Degree {degree})', color='green')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Fitting')
plt.show()
