import sys

N, price = [int(i) for i in input().split()]
coins = [int(sys.stdin.readline()) for _ in range(N)]

coins = reversed(coins)

total = 0
ans = 0
while (total < price):
    for coin in coins:
        if total + coin <= price:
            num = (price - total) // coin
            total += num * coin
            ans += num
            break

print(ans)