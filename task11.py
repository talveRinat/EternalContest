def sum_inverse(l, r, p):
    # инициализируем сумму
    total = 0
    # вычисляем сумму x^(p-2) по модулю p
    for x in range(l, r + 1):
        total += pow(x, p - 2, p)
    # возвращаем сумму по модулю p
    return total % p


l, r, p = map(int, input().split())
print(sum_inverse(l, r, p))
