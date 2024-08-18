import sys

n = int(sys.stdin.readline())
lst1 = sorted(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())
lst2 = list(map(int, sys.stdin.readline().split()))

for i in lst2:
    result = 0
    left = 0
    right = n-1
    mid = n//2

    while left <= right:
        if lst1[mid] == i:
            result = 1
            break
        elif lst1[mid] > i:
            right = mid - 1
            mid = (right + left) // 2
        elif lst1[mid] < i:
            left = mid + 1
            mid = (right + left) // 2

    print(result)