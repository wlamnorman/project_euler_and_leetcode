def primes_up_to(n: int) -> list[int]:
    # could use sieve for efficiency
    found_primes = []
    for candidate in range(2, n + 1):
        if not any(
            candidate % prime == 0
            for prime in found_primes
            if prime * prime <= candidate
        ):
            found_primes.append(candidate)

    return found_primes


print(sum(primes_up_to(2_000_000)))
