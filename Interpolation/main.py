import math
import numpy as np
from numpy import linalg as LA
from numpy.linalg import norm, inv
import matplotlib
from matplotlib import pyplot as plt
import matplotlib.colors as mcolors


def equidistant(num_points):
    return np.linspace(-2, 2, num_points + 1)


def chebyshev_vals(num_points):
    arr = []
    for j in range(num_points + 1):
        arr.append(2 * math.cos((((2 * j) + 1) / ((2 * num_points) + 2)) * math.pi))
    return arr
    #0.5 * (a + b) + 0.5 * (b - a) * math.cos((((2 * i) + 1) / ((2 * k) + 2)) * math.pi)


def gaussian(input_val):
    sigma = math.sqrt(0.2)
    mu = 0.0
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-(1 / 2) * (((input_val - mu) ** 2) / (sigma ** 2)))


def lagrange_basis(j, k, input_val):
    equidistant_array = equidistant(k)
    lx = 1
    for m in range(0, k + 1):
        if m != j:
            lx = lx * (input_val - equidistant_array[m])/(equidistant_array[j] - equidistant_array[m])
    return lx


def lagrange_basis_chebyshev(j, k, input_val):
    chebyshev_array = chebyshev_vals(k)
    lx = 1
    for m in range(0, k + 1):
        if m != j:
            lx = lx * (input_val - chebyshev_array[m]) / (chebyshev_array[j] - chebyshev_array[m])
    return lx


def lagrange(k, input_val):
    equidistant_array = equidistant(k)
    lx = 0
    for j in range(0, k + 1):
        lx = lx + gaussian(equidistant_array[j]) * lagrange_basis(j, k, input_val)
    return lx


def lagrange_chebyshev(k, input_val):
    chebyshev_array = chebyshev_vals(k)
    lx = 0
    for j in range(0, k + 1):
        lx = lx + gaussian(chebyshev_array[j]) * lagrange_basis_chebyshev(j, k, input_val)
    return lx


k1 = 5
k2 = 9

x_vals = []
g1 = []
l1 = []
l2 = []
l3 = []
norm_arr1 = []
norm_arr2 = []
norm_arr3 = []

for i in range(100):
    x_vals.append(float(4 * (i / 100)) - 2)

for i in range(100):
    g1.append(gaussian(x_vals[i]))
    l1.append(lagrange(k1, x_vals[i]))
    l2.append(lagrange(k2, x_vals[i]))
    l3.append(lagrange_chebyshev(k1, x_vals[i]))

# Quantifying discrepancy:

for i in range(len(x_vals)):
    norm_arr1.append(g1[i] - l1[i])
    norm_arr2.append(g1[i] - l2[i])
    norm_arr3.append(g1[i] - l3[i])

equidistantNorm1 = LA.norm(norm_arr1)
chebyshevNorm = LA.norm(norm_arr2)
equidistantNorm2 = LA.norm(norm_arr3)

print('\n6 equidistant:')
print(f'||g(x) - L(x)|| = {equidistantNorm1:.2}')
print('\n6 chebyshev:')
print(f'||g(x) - Lc(x)|| = {chebyshevNorm: .2}')
print('\n10 equidistant:')
print(f'||g(x) - L(x)|| = {equidistantNorm2:.2}')

# Generating graph:

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.plot(x_vals, g1, color='red')
plt.plot(x_vals, l1, color='blue')
plt.plot(x_vals, l2, color='green')
plt.plot(x_vals, l3, color='cyan')
plt.scatter(equidistant(k1), np.zeros(k1 + 1), color='blue', marker="o")
plt.scatter(equidistant(k2), np.zeros(k2 + 1), color='green', marker="o")
plt.scatter(chebyshev_vals(k1), np.zeros(k1 + 1), color='cyan', marker="o")
plt.show()
