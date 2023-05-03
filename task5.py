start, end = list(map(int, input().split()))

result = []
if 0 >= start:
    result.append('0')

for num in range(1, 10):
    cur_num = str(num)
    while int(cur_num) <= end:
        if int(cur_num) >= start:
            result.append(cur_num)
        cur_num += f'{num}'

print(len(result))
