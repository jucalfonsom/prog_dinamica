import numpy as np

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

coeffs = np.polyfit(x, y, 1)
print(coeffs)