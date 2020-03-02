n = int(input())
numbers = [int(i) for i in input().split()]

dp = [0] * (n+1)

ans = -987654321
dp[0] = numbers[0]
for i in range(1, n):
    dp[i] = max(dp[i-1]+numbers[i], numbers[i])
    ans = max(ans, dp[i])
print(max(ans, dp[0]))