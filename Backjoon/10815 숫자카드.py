N = int(input())
cards = [int(i) for i in input().split()]
M = int(input())
checks = [int(i) for i in input().split()]

cards.sort()


def bi_search(arr, left, right, target):
    if left > right:
        return 0

    mid = (left + right) // 2

    if arr[mid] == target:
        return 1
    if arr[mid] < target:
        return bi_search(arr, mid + 1, right, target)
    else:
        return bi_search(arr, left, mid - 1, target)


for i in checks:
    print(bi_search(cards, 0, N - 1, i), end=' ')