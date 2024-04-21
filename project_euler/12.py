from itertools import count


def count_divisors_of(n: int) -> int:
    # assumes n > 1
    count = 0  # 1 and n always divide n
    for num in range(1, int(n**0.5) + 1):
        if n % num == 0:
            count += 1
    return 2 * count


test_cases = [(3, 2), (6, 4), (10, 4), (15, 4), (21, 4), (28, 6)]
for n, expected_output in test_cases:
    output = count_divisors_of(n)
    assert output == expected_output


for n in count(1):
    tn = n * (n + 1) // 2
    tn_divs = count_divisors_of(tn)
    if tn_divs >= 500:
        print(n, tn)
        break
