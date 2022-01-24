
def MaxSubSquare(R,C,M):
    S = []
    for i in range(R):
      temp = []
      for j in range(C):
        if i==0 or j==0:
          temp += M[i][j],
        else:
          temp += 0,
      S += temp,

    for i in range(1, R):
        for j in range(1, C):
            if (M[i][j] == 1):
                S[i][j] = min(S[i][j-1], S[i-1][j],
                            S[i-1][j-1]) + 1
            else:
                S[i][j] = 0
    

    max_of_s = S[0][0]
    for i in range(R):
        for j in range(C):
            if (max_of_s < S[i][j]):
                max_of_s = S[i][j]
    return max_of_s



M = [[1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]]

kq=MaxSubSquare(4,5,M)
print(kq)
