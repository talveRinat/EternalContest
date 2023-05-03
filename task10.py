n = int(input())
vertices = [tuple(map(int, input().split())) for i in range(n)]

x_sum = sum([vertex[0] for vertex in vertices])
x_avg = x_sum / n

print(x_avg)
