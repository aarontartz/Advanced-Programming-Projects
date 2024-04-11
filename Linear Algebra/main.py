import numpy as np

A = np.array([[1, 0, 3, 4], [0, 1, 3, -1], [3, -3, 0, 6], [0, 2, 4, -6]])
A = np.array([[0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1, 0, 3, 4], [0.0, 0, 1, 3, -1], [0.0, 3, -3, 0, 6], [0.0, 0, 2, 4, -6]])
P = np.array([[0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0],
              [0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0]])

N = 4
maxRow = 0
val = 0

a = np.copy(A)
for i in range(1, N + 1):
    maxRow = i
    val = a[i, i]
    for j in range(i + 1, N + 1):
        if val <= a[j, i]:
            val = a[j, i]
            maxRow = j
    if maxRow != i:
        a[[i, maxRow]] = a[[maxRow, i]]
    for j in range(i + 1, N + 1):
        for k in range(N, i - 1, -1):
            # print(f'a[{j},{k}] -= a[{i},{k}] * a[{j},{i}]/a[{i},{i}]')
            # print(f'  {a[j,k]} -= {a[i,k]} * {a[j,i]}/{a[i,i]}')
            a[j, k] -= a[i, k] * a[j, i] / a[i, i]
    # print(f'System after zeroing column {i}:\na:{a}\n\n')
print(f'a:{a}')

a = np.copy(A)
for i in range(1, N + 1):
    maxRow = i
    val = a[i, i]
    for j in range(i + 1, N + 1):
        if val <= a[j, i]:
            val = a[j, i]
            maxRow = j
    if maxRow != i:
        a[[i, maxRow]] = a[[maxRow, i]]
        P[[i, maxRow]] = P[[maxRow, i]]
        A[[i, maxRow]] = A[[maxRow, i]]
    for j in range(i + 1, N + 1):
        a[j, i] /= a[i, i]
        for k in range(i + 1, N + 1):
            # print(f'a[{j},{k}] -= a[{i},{k}] * a[{j},{i}]/a[{i},{i}]')
            # print(f'  {a[j,k]} -= {a[i,k]} * {a[j,i]}')
            a[j, k] -= a[i, k] * a[j, i]
print(f'L+U-I:{a}')

U = np.zeros(a.shape)
for i in range(1, N + 1):
    for j in range(i, N + 1):
        if j >= i:
            U[i, j] = a[i, j]
L = np.zeros(a.shape)
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if j < i:
            L[i, j] = a[i, j]
        elif j == i:
            L[i, j] = 1.0

print(f'P:{P}')

print(f'A:{A}')
print(f'LU:{np.matmul(L, U)}')

a = np.copy(A)
b = np.array([0.0, 6.0, 0.0, 4.0, 3.0])
print(f'b:{b}')
y = np.zeros(N + 1)
for i in range(1, N + 1):
    sum = 0.0
    print(sum)
    for k in range(1, i + 1):
        sum += L[i, k] * y[k]
    y[i] = b[i] - sum
print(f'y:{y}')

x = np.zeros(N + 1)
for i in range(N, 0, -1):
    sum = 0
    for k in range(i + 1, N + 1):
        sum += U[i, k] * x[k]
    x[i] = (1 / U[i, i]) * (y[i] - sum)
print(f'x:{x}')

print(f'Ax:{np.matmul(A[1:,1:],x[1:])}')
print(f'b:{b[1:]}')

xx = np.linalg.solve(A[1:,1:],b[1:])
print(f'x:{xx}')
