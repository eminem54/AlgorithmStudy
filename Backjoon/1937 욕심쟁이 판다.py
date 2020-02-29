import sys

sys.setrecursionlimit(40000)


N = int(input())
graph = []
dp = [[0] * N for _ in range(N)]
for i in range(N):
    graph.append([int(i) for i in input().split()])


def dfs(i, j):
    if dp[i][j]:
        return dp[i][j]

    dp[i][j] = 1
    val = graph[i][j]
    if i + 1 < N and graph[i + 1][j] > val:
        dp[i][j] = max(dp[i][j], dfs(i + 1, j)+1)
    if i - 1 >= 0 and graph[i - 1][j] > val:
        dp[i][j] = max(dp[i][j], dfs(i - 1, j)+1)
    if j + 1 < N and graph[i][j + 1] > val:
        dp[i][j] = max(dp[i][j], dfs(i, j + 1)+1)
    if j - 1 >= 0 and graph[i][j - 1] > val:
        dp[i][j] = max(dp[i][j], dfs(i, j - 1)+1)

    return dp[i][j]


answer = 0
for i in range(N):
    for j in range(N):
        answer = max(dfs(i, j), answer)

print(answer)