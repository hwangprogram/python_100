h, b, c, s = map(int, input().split())

ans = format(((h * b * c * s) / 8 / 1024 / 1024), '.1f')
print(ans, end=' ')
print('MB')