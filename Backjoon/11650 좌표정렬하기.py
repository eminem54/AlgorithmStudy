N = int(input())
numbers = []
for i in range(N):
    numbers.append([int(i) for i in input().split()])
numbers.sort()

for i in numbers:
    print(i[0], i[1])