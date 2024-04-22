def min_remove_to_make_valid(s: str) -> str:
    ids_to_remove = set()
    stack = []

    for idx, char in enumerate(s):
        if char == "(":
            stack.append(idx)
        elif char == ")":
            if stack:
                stack.pop()
            else:
                ids_to_remove.add(idx)

    ids_to_remove = ids_to_remove.union(set(stack))

    new_s = ""
    for idx, char in enumerate(s):
        if not idx in ids_to_remove:
            new_s += char

    return new_s


test_cases = [
    ("lee(t(c)o)de)", "lee(t(c)o)de"),
    ("a)b(c)d", "ab(c)d"),
    ("))((", ""),
    ("((())", "(())"),
    ("((()))", "((()))"),
    ("(a)(b))", "(a)(b)"),
    (")(()a)(b))", "(()a)(b)"),
]
for input, expected_output in test_cases:
    actual_output = min_remove_to_make_valid(input)
    assert actual_output == expected_output
