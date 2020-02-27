A, B, V = [int(i) for i in input().split()]

rest = V - A

per1 = A - B


def bi_search(left, right):
    if left > right:
        return 0
    mid = (left + right) // 2
    if rest / per1 <= mid and rest / per1 > mid - 1:
        return mid + 1

    elif rest / per1 < mid:
        return bi_search(left, mid - 1)
    else:
        return bi_search(mid + 1, right)


print(bi_search(0, V))