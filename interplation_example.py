import numpy as np
import matplotlib.pyplot as plt
import math
"""
x_points = [1, 3]
y_points = [1, 3]

x1, x2 = 1, 3
y1, y2 = 1, 3

Z = np.array([[1, x1], [1, x2]])

Y = np.array([y1, y2])

# Compute the A matrix and print it
A = np.linalg.solve(Z, Y)

print("A = ", A)

# Compyte one specific point (x=2)
a1, a2 = A
x_value = 2
y_value = a1 + a2 * x_value
print("At x = 2, y =", y_value)

x = np.linspace(0, 5, 100)
y = a1 + a2 * x
plt.plot(x, y)

plt.scatter(x_points, y_points, color='blue', label='Known Points')

plt.scatter(x_value, y_value, color='red', zorder=5, label=f'Interpolated Point (x={x_value}, y={y_value:.2f})')

plt.title('Line with Interpolated Point (red)')
plt.xlabel("x"),
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()
"""

# Quadratic Interpolation
x_points = [1, 3, 5]
y_points = [1, 3, 2]

x1, x2, x3 = 1, 3, 5
y1, y2, y3 = 1, 3, 2

Z = np.array([[1, x1, x1 ** 2],
              [1, x2, x2 ** 2],
              [1, x3, x3 ** 2]])
Y = np.array([y1, y2, y3])

A = np.linalg.solve(Z, Y)

print("A = ", A)

a1, a2, a3 = A

x = np.linspace(-10, 10, 400)
y = a1 + a2 * x + a3 * x**2

plt.scatter(x_points, y_points, color='blue', s=60, label='Known Points')

x_value = 4
y_value = a1 + a2 * x_value + a3 * x_value**2
print("At x = 4, y =", y_value)

plt.plot(x, y, label='y =')