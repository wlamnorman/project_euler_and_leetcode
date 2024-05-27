def can_swap(s1: str, s2: str) -> bool:
    s1_idx_to_char = {}
    s2_idx_to_char = {}
    i = 0

    if len(s1) != len(s2):
        return False

    for c1, c2 in zip(s1, s2, strict=True):
        if c1 != c2:
            s1_idx_to_char[i] = c1
            s2_idx_to_char[i] = c2
        i += 1

    if len(s1_idx_to_char.keys()) != 2 or len(s2_idx_to_char.keys()) != 2:
        return False

    for key, val in s1_idx_to_char.items():
        if key not in s2_idx_to_char.keys():
            return False
        if val not in s2_idx_to_char.values():
            return False

    return True


test_cases = [
    (("hej", "jeh"), True),
    (("keke", "koko"), False),
    (("Jajamens", "Jamajens"), True),
    (("Jajamensa", "Jamajens"), False),
]

for input, expected_output in test_cases:
    assert can_swap(*input) == expected_output
