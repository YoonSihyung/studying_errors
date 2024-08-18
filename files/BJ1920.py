import sys

n = int(sys.stdin.readline())
lst1 = sorted(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())
lst2 = list(map(int, sys.stdin.readline().split()))

for i in lst2:
    result = 0
    l = n
    find = lst1[:]

    while len(find) > 1:
        if len(find) == 2:
            if find[0] == i:
                result = 1
                break
        if find[n//2] == i:
            result = 1
            break
        elif find[n//2] > i:
            find = find[:n//2]
            n //= 2
        elif find[n//2] < i:
            find = find[n//2+1:]
            n //= 2

    print(result)