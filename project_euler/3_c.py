from typing import Generator

num = 600851475143


def generate_prime_factors(
    n_: int, start: int = 2, end: int | None = None
) -> Generator[int, None, None]:
    for candidate_factor in range(start, (n_ if end == None else end) + 1):
        if n_ % candidate_factor == 0:
            yield candidate_factor
            yield from generate_prime_factors(
                n_ // candidate_factor, candidate_factor, n_ // candidate_factor
            )
            break


print(max(generate_prime_factors(num)))
