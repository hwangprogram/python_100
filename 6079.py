n = int(input())
i = 1
sum = 0

while True:
    sum += i
    i += 1
    if sum >= n:
        break

print(i - 1)