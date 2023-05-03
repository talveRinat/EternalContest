lst = list(map(int, input().split()))
even = -1
odd = -1
count_of_even = 0

# Iterate over the input list to find the variables for replacement
# (even number on odd index and odd number on even index),
# and count the number of even elements
for index, elem in enumerate(lst):
    if elem % 2 == 0:
        count_of_even += 1
    if (index + 1) % 2 != 0:
        if elem % 2 == 0:
            odd = index + 1
    else:
        if elem % 2 != 0:
            even = index + 1

if even == -1 or odd == -1 or count_of_even != len(lst) // 2:
    print(-1, -1)
else:
    print(odd, even)
