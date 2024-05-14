import math
import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate
import multiprocessing as mp
from functools import partial
import time


def f(x):
    return np.sin(x ** 2)


def F(x):
    res = np.zeros_like(x)
    for i, val in enumerate(x):
        y, err = integrate.quad(f, 0, val)  # integrate.quad returns tuple
        res[i] = y
    return res  # result


def perc_error(approx, actual):
    return (abs(approx - actual) / actual) * 100


def serial_simpson(n, h, serial_sum):
    t0 = time.time()
    for i in range(1, n):
        serial_sum += simpson(i, h)
    serial_approx = ((h / 3) * serial_sum)
    t1 = time.time()
    error = perc_error(serial_approx, actual_val)
    elap_time = t1 - t0
    report_error = "{:e}".format(error)
    report_elap_time = "{:e}".format(elap_time)

    print("SERIAL")
    print("Simpson approximation: ", serial_approx)
    print(f"Percent error: {report_error}%")
    print(f"Serial elapsed time: {report_elap_time}s")
    return


def parallel_simpson(n, h, parallel_sum, print_en):
    # Multiprocess constants
    threads = mp.cpu_count()
    pool = mp.Pool(processes=threads)

    t0 = time.time()
    arr = pool.map(partial(simpson, h=h), range(1, n))
    parallel_sum += sum(arr)
    parallel_approx = ((h / 3) * parallel_sum)
    t1 = time.time()
    error = perc_error(parallel_approx, actual_val)
    elap_time = t1 - t0
    report_error = "{:e}".format(error)
    report_elap_time = "{:e}".format(elap_time)
    if print_en:
        print("\nPARALLEL")
        print("Simpson approximation: ", parallel_approx)
        # Serial or parallel must be losing some precision compared to the other:
        print(f"Percent error: {report_error}%")
        print(f"Parallel elapsed time: {report_elap_time}s\n")
    return h, error, elap_time


def simpson(val, h):
    if val % 2 == 0:
        return 2 * f(val * h)
    else:
        return 4 * f(val * h)


if __name__ == '__main__':
    # Graphing indefinite integral constants
    t0 = 0
    tf = 2 * np.pi
    X = np.arange(t0, tf, 0.01)

    # Simpson's Rule constants
    actual_val = 1 / 2 * math.sqrt(np.pi / 2)
    b = 1000
    a = 0
    serial_sum = f(a) + f(b)  # First and last values
    parallel_sum = f(a) + f(b)

    # Initialize data structure for different h values and corresponding error
    h_vals = []  # [(h, error, elapsed time), ...]

    # Serial
    n = 10000000
    h = (b - a) / n
    serial_simpson(n, h, serial_sum)

    # Parallel/Multiprocess
    n = 10000000
    h = (b - a) / n
    h_vals.append(parallel_simpson(n, h, parallel_sum, 1))  # 1 enables func to print data

    # Adding more values to parallel simpson value data structure
    for i in range(0, 7):  # **COMPUTER CANT HANDLE LARGER VALUES THAN n = 10**7 (already appended 10**7 above)
        for j in range(1, 5):  # for each power of 10, take 4 values increasing by multiple of 2.5
            n = int((2.5 * j) * 10 ** i)  # Changing magnitude of h by altering n (since h = (b - a) / n)
            h = (b - a) / n
            h_vals.append(parallel_simpson(n, h, parallel_sum, 0))
    # Takes about 30-45sec to run on a 2020 M1 Macbook Pro

    print(h_vals)

    # Generating plots
    plt.plot(X, F(X), 'blue')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Fresnel Sine Integral")

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    # (X, Y, Z) = (h, error, elapsed time)
    X = []
    Y = []
    Z = []
    for i in range(len(h_vals)):
        X.append(math.log(h_vals[i][0], 10))  # log base 10 of h
        Y.append(math.log(h_vals[i][1], 10))
        Z.append(math.log(h_vals[i][2], 10))
    ax.scatter3D(X, Y, Z, 'blue')
    ax.set_xlabel('h (h = 10^x)')
    ax.set_ylabel('Error % (% = 10^y)')
    ax.set_zlabel('Elapsed time (sec = 10^z)')
    ax.set_title('Multiprocessed Simpson Approximations')
    plt.show()

    # The 3D graph shows the relationship between the step value, percent error, and elapsed time. It's shown that
    # step value has an equal linear relationship with the percent error when using Simpson's Rule, as conveyed by the
    # relatively straight line depicted when viewing this 2D relationship (O(n)). However, the elapsed time it takes to
    # parallel process integral approximations using Simpson's Rule takes exponentially longer with each step, as seen
    # by the exponential curve when viewing the 2D relationship between these two values (O(2^n)).
