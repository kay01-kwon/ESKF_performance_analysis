import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from scipy.interpolate import interp1d

np.random.seed(0)
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x) + np.random.normal(0, 0.1, x.size)

window_size = 11
poly_order = 3
y_smooth = savgol_filter(y, window_size, poly_order)

plt.plot(x, y, label='Noisy Signal')
plt.plot(x, y_smooth, label='Smoothed Signal', color='red')
plt.grid(lw=2,ls=':')
plt.xlabel('Time Step')
plt.ylabel("Value")
plt.legend()
plt.show()