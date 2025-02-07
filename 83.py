from math import inf

matrix = []
with open('/Users/ismailgerman/Desktop/euler/matrix.txt', 'r') as file:
    for line in file:
        matrix.append(list(map(int, line.split(','))))

print(len(matrix))

dp = [[[inf for i in range(80)] for j in range(80)] for k in range(80*80)]

dp[0][0][0] = matrix[0][0]

for i in range(1,80*80):
    for j in range(80):
        for k in range(80):
            dp[i][j][k] = dp[i-1][j][k]
            if j-1 >= 0:
                dp[i][j][k] = min(dp[i][j][k], matrix[j][k] + dp[i-1][j-1][k])
            if j < 79:
                dp[i][j][k] = min(dp[i][j][k], matrix[j][k] + dp[i-1][j+1][k])
            if k-1 >= 0:
                dp[i][j][k] = min(dp[i][j][k], matrix[j][k] + dp[i-1][j][k-1])
            if k < 79:
                dp[i][j][k] = min(dp[i][j][k], matrix[j][k] + dp[i-1][j][k+1])

for matrix in dp:
    for row in matrix:
        print(row)
    print()
