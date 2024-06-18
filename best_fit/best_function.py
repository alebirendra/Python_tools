import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Sample data points
lst1 = [5810.78, 6421.90, 7097.30, 7843.73, 8668.66]
lsek = [5, 10, 15, 20, 25]
x = np.array(lsek)
y = np.array(lst1)

# Define candidate models
def linear_model(x, a, b):
    return a * x + b

def quadratic_model(x, a, b, c):
    return a * x**2 + b * x + c

def exponential_model(x, a, b):
    return a * np.exp(b * x)

def power_law(x, a, b):
    return a * np.power(x, b)

# Fit the power law function to the data
params, covariance = curve_fit(power_law, x, y)

# Fit candidate models to the data
popt_linear, _ = curve_fit(linear_model, x, y)
popt_quadratic, _ = curve_fit(quadratic_model, x, y)
popt_exponential, _ = curve_fit(exponential_model, x, y)
popt_power, _ = curve_fit(power_law, x, y)

# equation
linear_equation = f'y = {popt_linear[0]:.2f} x + {popt_linear[1]:.2f} '
quad_equation = f'y = {popt_quadratic[0]:.2f} x**2 + {popt_quadratic[1]:.2f}*x + {popt_quadratic[2]:.2f}'
exp_equation = f'y = {popt_exponential[0]:.2f} exp({popt_exponential[1]:.2f}*x) '
power_equation = f'y = {popt_power[0]:.2f} * x^({popt_power[1]:.2f}) '


# Calculate goodness of fit measures (R-squared)
def r_squared(y, y_pred):
    residual = y - y_pred
    rss = np.sum(residual**2)
    tss = np.sum((y - np.mean(y))**2)
    return 1 - (rss / tss)

y_linear = linear_model(x, *popt_linear)
y_quadratic = quadratic_model(x, *popt_quadratic)
y_exponential = exponential_model(x, *popt_exponential)
y_power = exponential_model(x, *popt_power)

r_squared_linear = r_squared(y, y_linear)
r_squared_quadratic = r_squared(y, y_quadratic)
r_squared_exponential = r_squared(y, y_exponential)
r_squared_power = r_squared(y, y_power)

# Select the best model based on R-squared
best_model = max([(r_squared_linear, 'Linear'), (r_squared_quadratic, 'Quadratic'), (r_squared_exponential, 'Exponential'),
                 (r_squared_power, 'Power')], key=lambda x: x[0])

print("Best-fit model:", best_model[1])

# Plot the scatter plot
plt.scatter(x, y, color='blue', label='Data')

# Plot the best-fit curve
if best_model[1] == 'Linear':
    print("Equation of best-fit curve:", linear_equation)
    plt.plot(x, linear_model(x, *popt_linear), color='red', label='Best-fit curve (Linear)')
elif best_model[1] == 'Quadratic':
    print("Equation of best-fit curve:", quad_equation)
    plt.plot(x, quadratic_model(x, *popt_quadratic), color='red', label='Best-fit curve (Quadratic)')
elif best_model[1] == 'Exponential':
    print("Equation of best-fit curve:", exp_equation)
    plt.plot(x, exponential_model(x, *popt_exponential), color='red', label='Best-fit curve (Exponential)')
else:
    print("Equation of best-fit curve:", power_equation)
    plt.plot(x, power_law(x, *popt_power), color='red', label='Best-fit curve (Power)')
    
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot with Best-fit Curve')
plt.legend()
plt.grid(True)
plt.show()
