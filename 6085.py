w, h, b = map(int, input().split())

ans = format(((w * h * b) / 8 / 1024 / 1024), ".2f")
print(ans, end=' ')
print('MB')