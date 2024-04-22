from itertools import count


def count_divisors(n: int):
    count = 1
    prime_n = 2
    while prime_n**2 <= n:
        if n % prime_n == 0:
            power = 0
            while n % prime_n == 0:
                n //= prime_n
                power += 1
            count *= power + 1
        prime_n += 1

    if n > 1:
        count *= 2

    return count


for n in count():
    # using the fact that n and n+1 are coprime
    if n % 2 == 0:
        tn_divs = count_divisors(n // 2) * count_divisors(n + 1)
    else:
        tn_divs = count_divisors(n) * count_divisors((n + 1) // 2)

    if tn_divs >= 500:
        tn = n * (n + 1) // 2
        print(n, tn)
        break
