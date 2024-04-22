target = 9
nums = [2, 7, 11, 15]


def two_sum(target: int, nums: list[int]) -> list[int]:
    vals = {}
    for idx, val in enumerate(nums):
        other = vals.get(target - val)
        if other is not None and idx != other:
            return sorted([idx, other])
        vals[val] = idx

    raise ValueError(
        "It is assumed that each input would have exactly one solution"
        ", and you may not use the same element twice."
    )


test_examples = [
    (9, [2, 7, 11, 15], [0, 1]),
    (6, [3, 2, 4], [1, 2]),
    (6, [3, 3], [0, 1]),
]
for target, nums, expected in test_examples:
    actual = two_sum(target, nums)
    assert actual == expected, f"{target}, {nums}, {actual}, {expected}"
