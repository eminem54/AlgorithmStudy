N = int(input())

priority = {}
data = []
for i in range(N):
    line = input().split()
    if line[0] in priority.keys():
        priority[line[0]] += 1
    else:
        priority[line[0]] = 1
    data.append([int(line[0]), priority[line[0]], line[1]])
    
data.sort()
for i in data:
    print(i[0], i[2])