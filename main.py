import numpy as np

A = "ASDFASDFASDFASDFASFDASFDSADASSDFADSFAASDF"
B = "ASDFADSFASDFSADFDFSDFASSDASDAFFDSSADFSDAF"
C = "ASDSDFASDFASFDASDFASDAFSADFSADFDSFSDAFSDF"

def sequence_alignment(a, b):
    dp = np.zeros((len(a),len(b)))
    #i indexes A, j indexes B, k indexes C
    for i in range(len(a)):
        for j in range(len(b)):
            if i == 0:
                dp[i,j] = -8 * j
            if j == 0:
                dp[i,j] = -8 * i
            if A[i] == B[j]:
                dp[i,j] = max(dp[i-1, j] - 8, dp[i,j-1] - 8, dp[i-1, j-1]+ 5)
            else:
                dp[i, j] = max(dp[i - 1, j] - 8, dp[i, j - 1] - 8, dp[i - 1, j - 1] - 4)


    print(dp)
    return 0

sequence_alignment(A,B)