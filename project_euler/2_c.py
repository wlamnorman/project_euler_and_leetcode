from typing import Generator


def gen_fibbonaci_seq(n: int) -> Generator[int, None, None]:
    if n < 0:
        raise ValueError("'n' must be a non-negative integer.")
    f0, f1 = 1, 2
    for _ in range(n):
        yield f0
        f0, f1 = f1, f0 + f1


ans = sum(n for n in gen_fibbonaci_seq(100) if n <= 4e6 and n % 2 == 0)
print(ans)
