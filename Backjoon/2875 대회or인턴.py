girl, boy, intern = [int(i) for i in input().split()]

ans = 0
for index in range(intern+1):
    if (boy - index) * 2 <= girl - intern + index:
        ans = max(ans, boy - index)
    else:
        ans = max(ans, (girl - intern + index) // 2)
print(ans)