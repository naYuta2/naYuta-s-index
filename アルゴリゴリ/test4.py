import matplotlib.pyplot as plt
import numpy as np

x_data = np.array([10, 15, 31, 42, 50, 62])
y_data = np.array([32.0, 30.8, 27.3, 24.2, 21.8, 19.3])

a = 34.65
b = -0.25

plt.figure(figsize = (8, 6))
plt.scatter(x_data, y_data, label='実測データ点', color='blue', marker='o')

x_line = np.linspace(np.min(x_data), np.max(x_data), 100)
y_line = a + b * x_line

plt.plot(x_line, y_line, label=f'y = 34.65 - 0.25x', color='red')
plt.title('Relationship between workpiece diameter and mounting pressure')
plt.xlabel('Work diameter x (mm)')
plt.ylabel('mounting pressure y (MPa)')
plt.legend()
plt.grid(True)

plt.show()