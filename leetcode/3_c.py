def lols(s: str) -> int:
    window = set()
    longest = 0
    left_idx = 0

    for right_idx in range((len(s))):
        while s[right_idx] in window:
            window.remove(s[left_idx])
            left_idx += 1

        window.add(s[right_idx])

        if (candidate := right_idx - left_idx + 1) > longest:
            longest = candidate

    return longest


test_cases = [
    ("hejhsan", 6),
    ("abcabcbb", 3),
    ("bbbb", 1),
    ("pwwkew", 3),
    ("a", 1),
    ("", 0),
]
for input, expected_output in test_cases:
    assert lols(input) == expected_output, f"input: {input}, output: {lols(input)}"
