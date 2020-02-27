N = int(input())
budget = [int(i) for i in input().split()]
total = int(input())

def bi_search(left, right):
    low = left
    high = right
    mid = (low+high) // 2
    ans = 0
    while(low <= high):
        mid = (low + high) // 2
        
        temp = 0
        for i in budget:
            if i < mid:
                temp += i
            else:
                temp += mid
        
        if temp == total:
            return mid
        
        if temp < total:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return ans

if sum(budget) < total:
        print(max(budget))
else:
    print(bi_search(0, max(budget)))