N = int(input())
numbers = [int(i) for i in input().split()]

answer = [numbers[0]]
size = 0
for i in range(1, N):
    if answer[-1] < numbers[i]:
        answer.append(numbers[i])
        continue

    for j in range(len(answer) - 1):
        if answer[j] <= numbers[i] <= answer[j + 1]:
            answer[j+1] = numbers[i]
            break
    else:
        answer[-1] = numbers[i]



print(len(answer))

"""
8
1 5 10 3 13 18 15 16
"""