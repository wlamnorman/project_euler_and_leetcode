# v1: allowing use of strings
# def is_palindrome(x: int) -> bool:
#     as_str = str(x)
#     return as_str == as_str[::-1]


# v2: keeping x as int
# def is_palindrome(x: int) -> bool:
#     if x < 0:
#         return False

#     order = 0
#     for n in range(100):
#         if x / 10**n < 1:
#             order = n
#             break

#     checker = {}
#     for n in reversed(range(0, order)):
#         x_ = x
#         for exponent, val in checker.items():
#             x_ -= val * 10**exponent
#         checker[n] = x_ // (10**n)

#     place_values = list(checker.values())

#     if len(place_values) % 2 == 1:
#         middle_val = place_values[len(place_values) // 2 :][0]

#         n_num = len(place_values)
#         left_of_middle = place_values[: n_num // 2]
#         right_of_middle = place_values[n_num // 2 + 1 :]

#         return left_of_middle == right_of_middle[::-1]

#     left_of_middle = place_values[: len(place_values) // 2]
#     right_of_middle = place_values[len(place_values) // 2 :]
#     return left_of_middle == right_of_middle[::-1]

# v3: simplified version of keeping x as int
def is_palindrome(x: int) -> bool:
    if x < 0:
        return False

    original = x
    reversed = 0

    while x > 0:
        reversed = reversed * 10 + x % 10
        print(reversed)
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

print("All tests passed!")
