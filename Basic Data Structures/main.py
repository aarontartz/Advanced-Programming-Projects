import numpy as np

K3 = np.array([[2, -1, 0],[-1, 2, -1], [0, -1, 2]])
T3 = np.array([[1, -1, 0],[-1, 2, -1], [0, -1, 2]])
U3 = np.copy(T3)
K4 = np.array([[2, -1, 0, 0],[-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 2]])
T4 = np.array([[1, -1, 0, 0],[-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 2]])
U4 = np.copy(T4)


def toeplitz_K3():
        U3[1] = U3[1] + U3[0]
        U3[2] = U3[2] + U3[1]
        
        U3_trans = np.copy(U3)
        U3_trans = np.transpose(U3_trans)
        
        # Verifying T3 = U3^T * U3
        print(T3)
        print(np.matmul(U3_trans, U3))
        
        U3_inv = np.copy(U3)
        U3_inv = np.linalg.inv(U3_inv)
        U3_inv = U3_inv.astype(int)
        
        # Verifying I3 = U3 * U3^-1
        print(np.matmul(U3, U3_inv))
        
        U3_inv_product = np.matmul(U3_trans, U3)
        U3_inv_product = np.linalg.inv(U3_inv_product)
        U3_inv_product = U3_inv_product.astype(int)
        
        T3_inv = np.copy(T3)
        T3_inv = np.linalg.inv(T3_inv)
        T3_inv = T3_inv.astype(int)
        
        # Verifying (U3^T * U3)^-1 = T3^-1 (Note: (U^T * U)^-1 = (U^-1)(U^-1)^T)
        print(U3_inv_product)
        print(T3_inv)


def toeplitz_K4():
        U4[1] = U4[1] + U4[0]
        U4[2] = U4[2] + U4[1]
        U4[3] = U4[3] + U4[2]
        
        U4_trans = np.copy(U4)
        U4_trans = np.transpose(U4_trans)
        
        # Verifying T4 = U4^T * U4
        print(T4)
        print(np.matmul(U4_trans, U4))
        
        U4_inv = np.copy(U4)
        U4_inv = np.linalg.inv(U4_inv)
        U4_inv = U4_inv.astype(int)
        
        # Verifying I4 = U4 * U4^-1
        print(np.matmul(U4, U4_inv))
        
        U4_inv_product = np.matmul(U4_trans, U4)
        U4_inv_product = np.linalg.inv(U4_inv_product)
        U4_inv_product = U4_inv_product.astype(int)
        
        T4_inv = np.copy(T4)
        T4_inv = np.linalg.inv(T4_inv)
        T4_inv = T4_inv.astype(int)
        
        # Verifying (U4^T * U4)^-1 = T3^-1 (Note: (U^T * U)^-1 = (U^-1)(U^-1)^T)
        print(U4_inv_product)
        print(T4_inv)


toeplitz_K3()
toeplitz_K4()

