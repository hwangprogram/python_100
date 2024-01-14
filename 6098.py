r = d = 1
arr = []

for i in range(10):
    arr.append([])
    for j in range(10):
        arr[i].append(0)

for i in range(10):
    arr[i] = list(map(int, input().split()))

arr[1][1] = 9
while True:
    if (arr[r][d + 1] == 0):
        d += 1
        arr[r][d] = 9
    elif (arr[r + 1][d] == 0):
        r += 1
        arr[r][d] = 9
    elif (arr[r][d + 1] == 2):
        d += 1
        arr[r][d] = 9
        break
    elif (arr[r + 1][d] == 2):
        r += 1
        arr[r][d] = 9
        break
    else:
        break

for i in range(10):
    for j in range(10):
        print(arr[i][j], end=' ')
    print()