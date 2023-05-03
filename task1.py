a, b, c, d = map(int, input().split())

result = a + c * (d - b) if b < d else a

print(result)
