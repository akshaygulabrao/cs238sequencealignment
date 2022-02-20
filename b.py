import numpy as np

a = "ACGTACGTACGT"
b = "AGTACCTACCGT"

S_minus = [0] * (len(a) + 1)
S_plus = [0] * (len(b) + 1)

def align(M,N):
    if M == 0:
        for j in range(len(N)):
            print(f'- {b[j]}')
    else:
        path(0,0,M,N)
def path(i1,j1,i2,j2):
    if i1 + 1 == i2 or j1 == j2:
        print(f'aligned pairs for max-score path from {i1},{j1} to {i2},{j2}')
    else:
        # find maximum path scores i1,j1
        mid = (i1 + i2) // 2
        S_minus[j1] = 0
        for j in range(j1 + 1, j2+1):
            S_minus[j] = S_minus[j - 1] - 8
        for i in range(i1 + 1, mid ):
            print(S_minus)
            s = S_minus[j1]
            S_minus[j1] = c = S_minus[j1] - 8
            for j in range(j1 + 1, j2 + 1):
                if a[i-1] == b[j-1]:
                    c = max(S_minus[j] - 8, s + 5, c - 8)
                else:
                    c = max(S_minus[j] - 8, s - 4, c - 8)
                s = S_minus[j]
                S_minus[j] = c
        print(S_minus)
        print('\n\n')
        S_plus[j2] = 0
        for j in reversed(range(j1,j2)):
            S_plus[j] = S_plus[j+1] - 8
        for i in reversed(range(mid - 1,i2+1)):
            print(S_plus)
            s = S_plus[j2]
            S_plus[j2] = c = S_plus[j2] - 8
            for j in reversed(range(j1,j2)):
                if a[i-1] == b[j-1]:
                    c = max(S_plus[j] - 8,s + 5, c - 8)
                else:
                    c = max(S_plus[j] - 8, s - 4, c - 8)
                s = S_plus[j]
                S_plus[j] = c
        candidate_moves = [S_plus[i] + S_minus[i] for i in range(j1,j2+1)]
        j = max(range(len(candidate_moves)), key=lambda x:candidate_moves[x])
        path(i1,j1,mid,j)
        path(mid,j,i2,j2)





align(len(a), len(b))