import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Sample data points
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])

# Reshape the data for sklearn
X = x[:, np.newaxis]

# Polynomial regression
degree = 2  # Choose the degree of the polynomial
poly_features = PolynomialFeatures(degree=degree)
X_poly = poly_features.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

# Extract coefficients
coefficients = model.coef_
intercept = model.intercept_

# Formulate equation
equation = f'y = {coefficients[2]:.2f}x^2 + {coefficients[1]:.2f}x + {intercept:.2f}'

print("Equation of best-fit curve:", equation)

# Plot the scatter plot
plt.scatter(x, y, color='blue', label='Data')

# Plot the best-fit curve
x_values = np.linspace(min(x), max(x), 100)
X_values = x_values[:, np.newaxis]
y_values = model.predict(poly_features.transform(X_values))
plt.plot(x_values, y_values, color='red', label='Best-fit curve')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot with Best-fit Curve')
plt.legend()
plt.grid(True)
plt.show()
