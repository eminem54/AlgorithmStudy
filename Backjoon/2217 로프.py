import sys

N = int(input())
lopes = [int(sys.stdin.readline()) for _ in range(N)]

lopes.sort(reverse=True)

answer = 0
for i, v in enumerate(lopes):
    if v * (i + 1) > answer:
        answer = v * (i + 1)

print(answer)


