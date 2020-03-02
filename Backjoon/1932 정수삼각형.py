step = int(input())

tri = []
for i in range(step):
    tri.append([int(i) for i in input().split()])
    
dp = [[0] * i for i in range(1, step+1)]

dp[0][0] = tri[0][0]
for i in range(1, step):
    for j in range(i+1):
        if j-1 < 0:
            dp[i][j] = dp[i-1][j] + tri[i][j]
        elif j==i:
            dp[i][j] = dp[i-1][j-1] + tri[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]
            
print(max(dp[step-1]))