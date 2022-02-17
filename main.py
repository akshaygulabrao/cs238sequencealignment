import numpy as np
import math

A = "ACGTACGTACGT"
B = "AGTACCTACCGT"

C = "ASDSDFASDFASFDASDFASDAFSADFSADFDSFSDAFSDF"

def sequence_alignment(a, b):
    dp = np.zeros((len(a),len(b)),dtype=object)
    #i indexes A, j indexes B, k indexes C
    dp[0,0] = (0,'begin')
    for i in range(len(a)):
        dp[i,0] = (-8 *i, 'begin')
        continue
    for j in range(len(b)):
        dp[0,j] = (-8 * j,'begin')
        continue
    for i in range(len(a)):
        for j in range(len(b)):
            if i == 0 or j == 0: continue
            if A[i] == B[j]:
                #convert to argmaxes and store tuple
                candidate_moves = [(dp[i-1,j][0] - 8,'up'),(dp[i,j-1][0] - 8,'left'), (dp[i-1,j-1][0]+5, 'upleft')]
                dp[i,j] = max(candidate_moves,key=lambda x: x[0])
            else:
                #convert to argmaxes and store tuple
                candidate_moves = [(dp[i - 1, j][0] - 8, 'up'), (dp[i, j - 1][0] - 8, 'left'), (dp[i - 1, j - 1][0] - 4, 'upleft')]
                dp[i, j] = max(candidate_moves, key=lambda x: x[0])

    # print(dp)
    return dp


print(sequence_alignment(A,B))



