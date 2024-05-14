import math
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp


def current_source(t):
    return 2 * math.exp(-3.0 * t)  # Amps


def diff_funcs(t, y):
    i, v = y  # Extracting i(t) and v(t) from argument y
    return[(v - (R * i)) / L, (current_source(t) - i) / C]
    # [i'(t), v'(t)]


t0 = 0  # Secs
tf = 10  # Secs
y0 = [0, 10]  # Initial conditions [Amps, Volts]
R = 3  # Ohms
L = 1  # Henry
C = 0.5  # Coulombs
t_vals = np.arange(t0, tf, 0.01)  # Evenly spaced vals between t0 and tf with h = 0.01
t_span = [t0, tf]

# ‘RK45’: Explicit Runge-Kutta fourth-order method
S = solve_ivp(diff_funcs, t_span, y0, method='RK45', t_eval=t_vals)

# Generating graphs

plt.rcParams["figure.figsize"] = [10.50, 6.50]
plt.rcParams["figure.autolayout"] = True

fig, ax1 = plt.subplots()
ax1.set_xlabel('t (s)')
ax1.set_ylabel('i(t) (A)', color='red')
lns1 = ax1.plot(S.t, S.y[0], color='red', label='i(t)', linewidth=2)
ax1.tick_params(axis='y', labelcolor='red')

ax2 = ax1.twinx()  # Instantiating second axis that shares same x-axis

ax2.set_ylabel('v(t) (V)', color='blue')  # x-label already defined in ax1
lns2 = ax2.plot(S.t, S.y[1], color='blue', label='v(t)', linewidth=2)
ax2.tick_params(axis='y', labelcolor='blue')

# To display both lines in same legend:
lns = lns1 + lns2
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=0)

fig.tight_layout()  # To fix right y-label potentially being clipped
plt.title('i(t) & v(t) vs t in RLC circuit')
plt.grid()
plt.show()
