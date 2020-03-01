N = int(input())
times = [int(i) for i in input().split()]

times.sort()

total = 0
acc = 0
for i in times:
    acc += i
    total += acc


print(total)