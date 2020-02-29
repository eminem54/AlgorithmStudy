N = int(input())
data = []
for i in range(N):
    line = input().split()
    data.append([-int(line[1]), int(line[2]), -int(line[3]), line[0]])

data.sort()
for i in data:
    print(i[3])
