N = int(input())
meet = []
for i in range(N):
    meet.append([int(i) for i in input().split()])

meet.sort(key=lambda x: (x[1], x[0]), reverse=True)
ans = 1
time = meet.pop()[1]
while meet:
    item = meet.pop()
    if item[0] >= time:
        ans += 1
        time = item[1]


print(ans)