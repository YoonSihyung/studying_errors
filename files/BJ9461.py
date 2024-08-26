import sys

t = int(sys.stdin.readline())
lst = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
lst += [0]*90
leng = 10

'''
조건문(if, for 등)을 다룰 때는 조건이 시시각각 변하는 지를 봐야 한다.
for _ in range(t):
    n = int(sys.stdin.readline())

    if n > len(lst):
        for i in range(len(lst), n):
            lst.append(lst[i] + lst[i-4])
'''

for _ in range(t):
    n = int(sys.stdin.readline())

    if n > leng:
        for i in range(leng, n):
            lst[i] = lst[i-1] + lst[i-5]
            leng += 1

    print(lst[n - 1])