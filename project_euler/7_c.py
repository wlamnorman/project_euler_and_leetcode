def nth_prime(n: int) -> int:
    found_primes = []
    candidate = 2
    while True:
        if not any(
            candidate % prime == 0
            for prime in found_primes
            if prime * prime <= candidate
        ):
            found_primes.append(candidate)

        if len(found_primes) == n:
            break

        candidate += 1
    return found_primes[-1]


test_cases = [(1, 2), (6, 13)]
for n, expected_output in test_cases:
    assert nth_prime(n) == expected_output

ans = nth_prime(10001)
print(ans)
