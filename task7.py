n = int(input())
a = list(map(int, input().split()))

def full_answer(count_of_members, members):
    counts = {num: 0 for num in range(1, count_of_members + 1)}
    for member in members:
        counts[member] += 1

    def is_sequence(sequence, sequence_len):
        unique_numbers = set()
        current_position = 1
        for _ in range(sequence_len):
            current_position = sequence[current_position - 1]
            if current_position in unique_numbers:
                return False
            unique_numbers.add(current_position)
            if current_position == 1:
                return len(unique_numbers) == sequence_len
        return False

    def answer():
        count_of_problems = 0
        place, number = None, None
        for key, value in counts.items():
            if count_of_problems > 2:
                return '-1 -1'
            if value == 0:
                number = key
                count_of_problems += 1
            elif value == 2:
                place = key
                count_of_problems += 1
            elif value > 2:
                count_of_problems += value
        if count_of_problems == 0:
            return '-1 -1'
        if count_of_problems == 2:
            for idx, current in enumerate(members):
                if current == place and idx + 1 != number:
                    changed_sequence = members[:]
                    changed_sequence[idx] = number
                    if is_sequence(changed_sequence, len(changed_sequence)):
                        return f'{idx+1} {number}'
        return '-1 -1'

    return answer()



full_answer(n, a)