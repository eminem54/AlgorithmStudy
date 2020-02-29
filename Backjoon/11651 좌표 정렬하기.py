N = int(input())
numbers = []
for i in range(N):
    numbers.append([int(i) for i in reversed(input().split())])
    
numbers.sort()

for i in numbers:
    print(i[1], i[0])