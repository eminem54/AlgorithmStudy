T = int(input())

dp = [1,1,1,2,2,3,4,5,7,9]
for i in range(10, 101):
    dp.append(dp[-1] + dp[-5])
    
for i in range(T):
    n = int(input())
    print(dp[n-1])
    