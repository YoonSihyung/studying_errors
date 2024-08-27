#끝자리가 1일 때, n-1의 가짓수와 똑같다.
#끝자리가 00일때, n-2의 가짓수와 똑같다.

import sys

n = int(sys.stdin.readline())
lst = [1, 2]
lst += [0] * (n-2)
#lst += [0] * n-2

for i in range(2, n):
    lst[i] = lst[i-1] + lst[i-2]

print(lst[n-1])