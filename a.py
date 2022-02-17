import numpy as np
A = "ACGTACGTACGT"
B = "AGTACCTACCGT"

def ALG_B(m,n,A,B):
    print(A,len(A),B,len(B))
    K = np.zeros((2,n+1))
    for i in range(len(K[0])):
        K[0][i] = i * -8
    for i in range(1,m+1):
        for j in range(1,n+1):
            if A[i-1] == B[j-1]:
                K[1][j] = max(K[0][j-1] + 5,K[1][j-1] - 8,K[0][j] - 8)
            else:
                K[1][j] = max(K[0][j-1] - 4,K[1][j-1] - 8,K[0][j] - 8)
        K[0] = K[1][:]
    return K[1][:]



def ALG_C(m,n,A,B):
    if n == 0: return ""
    elif m == 1:
        if A[0] in B:
            return A[0]
        else:
            return ""
    else:
        mid = m // 2
        L1 = ALG_B(mid,n,A[:mid],B[:])
        L2 = ALG_B(m-mid,n,A[:mid-1:-1],B[::-1])
        for j in range(n-1):
            print(L1[j] + L2[n-j])

ALG_C(len(A),len(B),A,B)





