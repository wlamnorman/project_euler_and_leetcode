from math import ceil


def largest_palindrome_product_v1(n_digit_nums: int) -> int:
    def is_palindrome_product(n: int, m: int) -> bool:
        p = str(n * m)
        if len(p) % 2 == 0 and p[: len(p) // 2] == p[len(p) // 2 :][::-1]:
            return True
        elif len(p) % 2 == 1 and p[: ceil(len(p) / 2)] == p[ceil(len(p) / 2) :][::-1]:
            return True
        return False

    max_palindrome_product_seen = 0
    for i in range(int("9" * n_digit_nums), int("9" * (n_digit_nums - 1)), -1):
        for j in range(int("9" * n_digit_nums), i - 1, -1):
            if is_palindrome_product(i, j) and i * j > max_palindrome_product_seen:
                max_palindrome_product_seen = i * j
    return max_palindrome_product_seen


ans = largest_palindrome_product_v1(n_digit_nums=3)
print(ans)
