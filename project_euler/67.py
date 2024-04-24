with open("0067_triangle.txt") as file:
    triangle: list[list[int]] = [
        [int(x) for x in line.split(" ")] for line in file.read().splitlines()
    ]


def max_path_sum(triangle: list[list[int]]):
    n_rows = len(triangle)
    for row in range(n_rows - 2, -1, -1):
        n_cols = len(triangle[row])
        for col in range(n_cols):
            triangle[row][col] += max(
                triangle[row + 1][col], triangle[row + 1][col + 1]
            )
    return triangle[0][0]


print(max_path_sum(triangle))
