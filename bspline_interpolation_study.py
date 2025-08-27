import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

x = np.arange(0, 2*np.pi, 1)
y = np.sin(np.pi*x)

bspl = make_interp_spline(x, y, k=3)
der = bspl.derivative()

xx = np.arange(0, np.pi, 0.01)
yy = bspl(xx)
dydx =der(xx)

plt.plot(xx,yy,label='value')
plt.plot(xx, dydx, label='derivative')
plt.legend()
plt.show()