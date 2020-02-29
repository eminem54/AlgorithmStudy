N = int(input())

numbers = {}

for i in range(N):
    number = int(input())

    if number in numbers.keys():
        numbers[number] += 1
    else:
        numbers[number] = 1

data = []
for i, (k, v) in enumerate(numbers.items()):  # 장수, 숫자
    data.append([v, k])

data.sort(key=lambda x: (-x[0], x[1]))

print(data[0][1])
