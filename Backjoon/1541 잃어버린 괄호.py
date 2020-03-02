text = input()

minus = text.split('-')
if len(minus) == 0:
    print(0)
    exit()
    
    
summ = 0
if minus[0].isdigit():
    summ = int(minus[0])
else:
    for i in minus[0].split('+'):
        summ += int(i)

for num in minus[1:]:
    if num.isdigit():
        summ -= int(num)
    else:
        plus = num.split('+')
        for number in plus:
            summ -= int(number)
            
print(summ)