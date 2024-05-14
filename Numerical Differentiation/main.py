import math
from matplotlib import pyplot as plt


def function(x):
    a = 1
    b = math.cos(x)
    for j in range(1, 6):
        c = b
        # Plotting only real part of square root:
        if (a * b) >= 0:
            b = math.sqrt(a * b)
        else:
            b = 0
        a = (a + c) / 2
    if a == 0:
        return
    else:
        return 2 * math.atan(1.0 / a)


def cdiff(n):
    if function(n + h) is None:
        a = math.pi
    else:
        a = function(n + h)
    if function(n - h) is None:
        b = math.pi
    else:
        b = function(n - h)
    return float((a - b) / (2 * h))


x_vals = []
x_vals_diff = []
f = []
f_diff = []
h = float(2 * math.pi * (1 / 500))

for i in range(501):
    x_vals.append(float(2 * math.pi * (i / 500)))
    if (i != 0) & (i != 500):
        x_vals_diff.append(float(2 * math.pi * (i / 500)))
        # Differential uses +/- h, so must ignore first and last values to prevent
        # using null value

for i in range(501):
    f.append(function(x_vals[i]))

for i in range(1, 500):
    f_diff.append(cdiff(x_vals[i]))
    # Differential uses +/- h, so must ignore first and last values to prevent
    # using null value

print("Approximate value of f'(0.25): ", cdiff(0.25))

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.plot(x_vals, f, color='red', label='f(x)')
plt.plot(x_vals_diff, f_diff, color='blue', label="f'(x)")
plt.legend()
plt.show()
