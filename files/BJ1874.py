import sys
from collections import deque

n = int(sys.stdin.readline())
stack = deque()
answer = [] #'+'와 '-'를 넣는 리스트이다. 마지막에 한 번에 출력한다.
level = 1 #이제 어떤 숫자를 push 해야 하는 지를 표시한다.
lock = False

for _ in range(n):
    number = int(sys.stdin.readline()) #pop해야 하는 숫자를 받는다.

    if len(stack) == 0: #stack이 비어 있다면, 우선 채워야 한다.
        if level <= n:
            stack.append(level)
            answer.append('+')
            level += 1

    if stack[-1] > number: #만약 pop해야 하는 숫자가 stack 꼭대기 숫자보다 작다면, 이 수열은 stack으로 만들 수 없는 수열이다.
        lock = True
    elif stack[-1] < number: #만약 pop해야 하는 숫자가 stack 꼭대기 숫자보다 크다면, stack에 number에 닿을 때까지 계속 채운다.
        while level <= number:
            if level <= n:
                stack.append(level)
                answer.append('+')
                level += 1

    if stack[-1] == number: #위의 if-elif 문에서 stack의 꼭대가 숫자가 계속 바뀌므로 elif로 처리하지 않고, if문으로 처리해 계속 접근하도록 한다.
        stack.pop()
        answer.append('-')

if lock:
    print('NO')
else:
    for i in answer:
        print(i)