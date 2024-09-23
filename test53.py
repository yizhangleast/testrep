import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb
from scipy import interpolate



x = np.linspace(0,9,10)
x1 = np.linspace(0,9,91)
y = comb(9,range(10))*pow(0.5,9)
f = interpolate.interp1d(x, y, kind = 'quadratic')
y1 = f(x1)
plt.plot(x,y)
plt.plot(x1,y1)
plt.show()