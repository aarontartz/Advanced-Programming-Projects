from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
colors = ['green','cyan','blue','orange','purple','red','yellow']


def P(n, x):
    if (n == 0):
        return 1.0
    elif (n == 1):
        return float(x)
    else:
        return (((((2 * n) - 1) / n) * x * P(n - 1, x)) - ((n - 1) / n) * P(n - 2, x))

# Printing values of Pn(x) in intervals of delta x = 0.5
for n in range(6):
    print(P(n, -1.0), P(n, -0.5), P(n, 0), P(n, 0.5), P(n, 1.0))

# Creating plot
plt.title("Legendre Polynomials, $P_n(x)$")
plt.xlabel("x")
plt.ylabel("$P_n(x)$")
plt.grid()
for n in range(6):
    for x in range(999):
        if (x < 500):
            x = (x / 500) - 1
        else:
            x = x - 500
            x = (x / 500)
        plt.plot(x, P(n, x), '.', color=colors[n], label='n='+str(n))
