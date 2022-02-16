A = "ACGTACGTACGT"
B = "AGTACCTACCGT"

def ALG_B(m,n,A,B):
    print(A,len(A),B,len(B))
    K = [[0]*(n+1)] * 2
    for i in range(1,m+1):
        K[0] = K[1][:]
        for j in range(1,m+1):
            if A[i-1] == B[j-1]:
                K[1][j] = max(K[0][j-1] + 5,K[1][j-1] - 8,K[0][j] - 8)
            else:
                K[1][j] = max(K[0][j-1] - 4,K[1][j-1] - 8,K[0][j] - 8)
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
        L2 = ALG_B(m-mid,n,A[mid+1::-1],B[::-1])
        print(L1,L2)
        M = 0
        for j in range(n):
            if M < (L1[j] + L1[(n-j])





print(ALG_C(len(A),len(B),A,B))





