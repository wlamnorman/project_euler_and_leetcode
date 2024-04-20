class Solution:
    def lengthOfLastWord(self, s: str) -> int:
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
for example, expected in test_examples:
    assert (
        len(
            example.rstrip(" ").rsplit(
                " ",
            )[-1]
        )
        == expected
    )
