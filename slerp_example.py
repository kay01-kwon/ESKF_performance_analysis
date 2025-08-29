import numpy as np

t = np.arange(0, 0.1, 0.01)
x = np.sin(2 * np.pi * t)

N = len(t)
for i, x_i in enumerate(x):
    if i+1 < N:
        print(i, x[i+1])