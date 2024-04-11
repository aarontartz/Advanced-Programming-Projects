import math
import numpy as np
from numpy.linalg import norm, inv
import matplotlib
from matplotlib import pyplot as plt
import matplotlib.colors as mcolors
import scipy
from scipy.optimize import curve_fit
import csv


def func(x, a, b, c):
    return a * np.exp(-b * x) + c


with open('/Users/aarontartz/Desktop/2N2222.csv', 'r') as f: # Change file directory as needed
    reader = csv.reader(f)
    data = list(reader)
    data_array = np.array(data, dtype=float)
xdata = data_array[:, 0]
ydata = data_array[:, 1]

popt = curve_fit(func, xdata, ydata)[0]
pcov = curve_fit(func, xdata, ydata)[1]

#print(f'popt:{popt}')

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.scatter(xdata, ydata, color='blue', marker="o")
plt.plot(xdata, func(xdata, *popt), color='red', label='Model Function')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Non-Linear Regression Relation: %5.3f * e^((-%5.3f) * x) + %5.3f:' % tuple(popt))
plt.legend()
plt.grid()

print("One standard deviation errors:", np.sqrt(np.diag(pcov)))
print("Estimate for Vce when Ib = 3.1mA:", func(3.1, popt[0], popt[1], popt[2]), "V")
plt.show()
