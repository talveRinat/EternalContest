_, cnt_opers = list(map(int, input().split()))
nums = list(input().split())

operations = []

# Для кажого числа в списке чисел:
for num in nums:
    # Для каждого разряда в числе
    for digit_position in range(len(str(num))):
        # Получить ЦИФРУ по разряду
        digit = str(num)[-(digit_position + 1)]
        # Высчитать разницу, если эту цифру в этом разряде поменять на 9
        operation = 10 ** digit_position * (9 - int(digit))
        # Добавить результат в список
        operations.append(operation)
# Отсортировать список по убыванию
operations.sort(reverse=True)
# Вернуть сумму по количеству разрешенных операций в кейсе
print(sum(operations[:cnt_opers]))
