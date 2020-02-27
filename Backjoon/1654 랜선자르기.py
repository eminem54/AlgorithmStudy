K, N = [int(i) for i in input().split()]
lopes = []
for i in range(K):
    lopes.append(int(input()))
    
low = 1
high = max(lopes)
ha = 0

while (low <= high):
    mid = (low + high) // 2
    
    goal = 0

    for i in lopes:
        goal += i//mid
        
    if goal >= N:
        ha = mid
        low = mid + 1
    else:
        high = mid - 1
print(ha)