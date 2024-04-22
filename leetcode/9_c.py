def is_palindrome(x: int) -> bool:
    if x < 0:
        return False

    original = x
    reversed = 0

    while x > 0:
        reversed = reversed * 10 + x % 10
        x //= 10

    return original == reversed


test_cases = [
    (121, True),
    (-121, False),
    (10, False),
    (22, True),
    (1, True),
    (1001, True),
    (102, False),
]
for num, expected in test_cases:
    assert is_palindrome(num) == expected
