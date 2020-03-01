# 500엔, 100엔, 50엔, 10엔, 5엔, 1
price = 1000 - int(input())

coins = [500, 100, 50, 10, 5, 1]
ans = 0
while price != 0:
    for coin in coins:
        if price - coin >= 0:
            per = price // coin
            price -= per * coin
            ans += per
            break
            
print(ans)