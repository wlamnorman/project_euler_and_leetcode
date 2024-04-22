def is_palindrome_product(n: int, m: int) -> bool:
    product_str = str(n * m)
    return product_str == product_str[::-1]


def largest_palindrome_product(n_digit_nums: int) -> int:
    max_palindrome_product_seen = 0
    lower_bound = 10 ** (n_digit_nums - 1)
    upper_bound = 10**n_digit_nums - 1

    for i in range(upper_bound, lower_bound, -1):
        for j in range(i, lower_bound - 1, -1):
            if (product := i * j) <= max_palindrome_product_seen:
                break  # break early as products are decreasing since we are looping with decreasing j
            if is_palindrome_product(i, j):
                max_palindrome_product_seen = product

    return max_palindrome_product_seen


print(largest_palindrome_product(n_digit_nums=3))
