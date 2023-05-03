_, t = map(int, input().split())
floors = list(map(int, input().split()))
leaving_colleague = int(input())

leaving_colleague -= 1
all_floors = max(floors) - min(floors)
cond2 = 2*max(floors) - floors[leaving_colleague] - min(floors)
cond1 = floors[leaving_colleague] - 2*min(floors) + max(floors)

if t >= abs(max(floors) - floors[leaving_colleague]):
    print(all_floors)
elif t >= abs(floors[leaving_colleague] - min(floors)):
    print(all_floors)
else:
    print(min(cond1, cond2))
