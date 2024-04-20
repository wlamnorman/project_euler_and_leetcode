def sum_square_diff(n: int) -> int:
    square_of_sum = (n * (n + 1) / 2) ** 2
    sum_of_squares = sum([x**2 for x in range(n + 1)])
    return int(square_of_sum - sum_of_squares)


ans = sum_square_diff(100)
print(ans)
