h, w = map(int, input().split())

arr = []

for i in range(h):
    arr.append([])
    for j in range(w):
        arr[i].append(0)



n = int(input())

for i in range(n):
    l, d, y, x = map(int, input().split())
    if d == 0:
        for j in range(l):
            arr[y-1][x-1+j] = 1
    elif d == 1:
        for j in range(l):
            arr[y-1+j][x-1] = 1

for i in range(h):
    for j in range(w):
        print(arr[i][j], end=' ')
    print()