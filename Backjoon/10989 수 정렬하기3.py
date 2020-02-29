import sys
N = int(input())
numbers = [0 for i in range(10001)]
for i in range(N):
    numbers[int(sys.stdin.readline())] += 1

for i in range(10001):
    if numbers[i] != 0:
        for j in range(numbers[i]):
            print(i)