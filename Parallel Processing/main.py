import time
import numpy as np
import multiprocessing as mp
from functools import partial


def inner_prod(k, i, j, A, B):
    return A[i, k] * B[k, j]


if __name__ == '__main__':
    M = 25
    N = 5
    P = 20
    A = np.random.rand(M, N)
    B = np.random.rand(N, P)
    threads = mp.cpu_count()
    pool = mp.Pool(processes=threads)

    C_serial = np.zeros((M, P))
    C_parallel = np.zeros((M, P))

    # Serial processing:
    t0 = time.time()
    for i in range(M):
        for j in range(P):
            sum_val = 0.0
            for k in range(N):
                sum_val += A[i, k] * B[k, j]
            C_serial[i][j] = sum_val
    t1 = time.time()
    print(f"Serial: elapsed time is {t1 - t0:.15f}s")

    # Parallel processing:
    t0 = time.time()
    for i in range(M):
        for j in range(P):
            C_parallel[i][j] = sum(pool.map(partial(inner_prod, i=i, j=j, A=A, B=B), range(N)))
    t1 = time.time()
    print(f"Parallel: elapsed time is {t1 - t0:.15f}s")

    np.testing.assert_allclose(C_serial, C_parallel, rtol=1e-5, atol=0)  # verifies both arrays are equal
