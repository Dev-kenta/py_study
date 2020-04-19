import matplotlib.pyplot as plt
import numpy as np

x = np.array(['202001', '202002', '202003', '202004', '202005', '202006'])
y = np.array([270000, 270000, 275000, 270000, 280000, 275000])

plt.title("Month - Salary")
plt.xlabel("Month")
plt.ylabel("Salary")
plt.grid(True)

plt.bar(x, y)
plt.show()