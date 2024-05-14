import numpy as np
from matplotlib import pyplot as plt
import pickle


def dft(func_vals):  # discrete fourier transform
    N = len(func_vals)
    n_vals = np.arange(N)
    #print(n_vals)
    k = n_vals.reshape((N, 1))  # transform to N x 1 column vector
    e = np.exp(-1j * 2 * np.pi * k * n_vals / N)
    X = np.dot(e, func_vals)
    return X


sig_vals = []
with (open("/Users/aarontartz/Downloads/x.pkl", "rb")) as openfile:
    while True:
        try:
            sig_vals.append(pickle.load(openfile))
        except EOFError:
            break

sr = 256  # Hz
tf = 6  # secs
num_pkl_vals = sr * tf
period = 1 / sr
t_vals = np.arange(0, tf, period)

fourier_vals = dft(sig_vals[0])
discrete_vals = []  # 6 vals for each sec period of signal
decoded_str = ""

# Generate plots
plt.subplot(241)  # .subplot(rows * 100 + columns * 10 + index)
plt.plot(t_vals, sig_vals[0], 'blue')
plt.xlabel('Time (sec)')
plt.ylabel('Amplitude')

for i in range(6):
    sum_freq = 0
    # First set values for the plot
    discrete_vals.append(dft(sig_vals[0][(sr * i):(sr * (i + 1))]))
    N = len(discrete_vals[i])
    n = np.arange(N)
    T = N / sr
    freq = n / T
    n_oneside = N // 2  # floor division
    f_oneside = freq[:n_oneside]  # getting the one side frequency
    X_oneside = discrete_vals[i][:n_oneside] / n_oneside  # normalize the amplitude
    # Then decode values of each plot
    for j in range(len(X_oneside)):
        if abs(X_oneside[j]) > 0.8:
            sum_freq += f_oneside[j]
    print("Decimal: ", sum_freq, " Hex: ", hex(int(sum_freq)))
    text = str(hex(int(sum_freq)))
    decoded_str += text[2:]  # used to decode sequence later
    # Then generate visual plot
    plt.subplot(242 + i)
    plt.stem(f_oneside, abs(X_oneside), 'red', markerfmt=" ", basefmt="red")
    plt.xlabel("Freq (Hz) (Letter " + str(i + 1) + ")")
    plt.ylabel("Amplitude")

print("Secret word: ", bytearray.fromhex(decoded_str).decode())
plt.tight_layout()
plt.show()
