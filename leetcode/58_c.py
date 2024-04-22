def lengthOfLastWord(s: str) -> int:
    return len(
        s.rstrip(" ").rsplit(
            " ",
        )[-1]
    )


test_examples = [
    ("Hello World", 5),
    ("   fly me   to   the moon  ", 4),
    ("luffy is still joyboy", 6),
]
for input, expected_output in test_examples:
    assert lengthOfLastWord(input) == expected_output
