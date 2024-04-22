from typing import Generator
from tqdm import tqdm


def collatz_seq(n: int) -> Generator[int, None, None]:
    yield n
    while n != 1:
        n = n // 2 if (n % 2 == 0) else 3 * n + 1
        yield n


def len_collatz_seq(n: int, cache: dict) -> int:
    # using memoization (efficient for repeated calculations for different initial values)

    count = 0
    seq = []
    for n_ in collatz_seq(n):
        if n_ not in cache:
            seq.append(n_)
        else:
            count = cache[n_]
            break

    while seq:
        n_ = seq.pop()
        count += 1
        cache[n_] = count

    return cache[n]


assert list(collatz_seq(13)) == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert len_collatz_seq(13, {}) == 10

COLLATZ_LEN_CACHE = dict()
max_len = 0
max_idx = 0
for n in tqdm(range(1, 1_000_000)):
    seq_len = len_collatz_seq(n, COLLATZ_LEN_CACHE)

    if seq_len > max_len:
        max_len = seq_len
        max_idx = n

print(max_idx)
print(max_len)
