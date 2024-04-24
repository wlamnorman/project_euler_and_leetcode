triangle_str = """3
7 4
2 4 6
8 5 9 3"""
triangle = [[int(x) for x in line.split(" ")] for line in triangle_str.splitlines()]

### the solution here is ineffective due to copying and using brute force
### see problem 0067 for a more efficient version that uses backtracking


def next_choices(triangle: list[list[int]], row: int, row_idx: int):
    next_row = triangle[row + 1]
    return next_row[row_idx : row_idx + 2]


assert next_choices(triangle, 0, 0) == [7, 4]
assert next_choices(triangle, 1, 0) == [2, 4]
assert next_choices(triangle, 1, 1) == [4, 6]


def recursive_path_search(
    triangle: list[list[int]], row_num: int = 0, row_idx: int = 0, seq: list = []
) -> list[list[int]]:
    seq.append(triangle[row_num][row_idx])
    if row_num == len(triangle) - 1:
        return [seq.copy()]

    paths = []
    for d_idx, _ in enumerate(next_choices(triangle, row_num, row_idx)):
        new_paths = recursive_path_search(
            triangle, row_num + 1, row_idx + d_idx, seq.copy()
        )
        paths.extend(new_paths)

    return paths


# test that all paths are included
expected_paths = [
    [3, 7, 2, 8],
    [3, 7, 2, 5],
    [3, 7, 4, 5],
    [3, 7, 4, 9],
    [3, 4, 4, 5],
    [3, 4, 4, 9],
    [3, 4, 6, 9],
    [3, 4, 6, 3],
]
print(triangle)
for path, expected_path in zip(
    recursive_path_search(triangle, seq=[]), expected_paths, strict=True
):
    # assert len(path) == len(triangle)
    for val, expected_val in zip(path, expected_path, strict=True):
        assert val == expected_val, ("%d %d", val, expected_val)


triangle_str = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
triangle = [[int(x) for x in line.split(" ")] for line in triangle_str.splitlines()]

max_path_weight, max_path = 0, []
for path in recursive_path_search(triangle, seq=[]):
    assert len(path) == len(triangle)
    path_weight = sum(path)
    if path_weight > max_path_weight:
        max_path_weight = path_weight
        max_path = path

print(max_path_weight, max_path)
