N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

A.sort()
B.sort(reverse=True)
result = 0
for i in range(len(A)):
    result += A[i] * B[i]
    
print(result)