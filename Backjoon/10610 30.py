N = input()

total = 0
for i in N:
    total += int(i)

num = [i for i in N]
num.sort(reverse=True)
    
if total % 3 != 0 or num[-1] != '0':
    print(-1)
    exit(0)

print(int(''.join(num)))



    
    