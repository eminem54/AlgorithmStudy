N = int(input())
rgb = []

for i in range(N):
    rgb.append([int(i) for i in input().split()])
    
dp = [[0 for i in range(3)] for j in range(1001)]


for i in range(1, N+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i-1][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i-1][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i-1][2]
    
print(min(dp[N]))