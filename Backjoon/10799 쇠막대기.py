"""실패"""

def main():
    paren = input()
    mystack = []
    ans = 0
    for ch in paren:
        if ch == '(':
            mystack.append(ch)

        if ch == ')':
           ans += len(mystack) - 1
           print(len(mystack) - 1)

           mystack.pop()

    print(ans)

main()


