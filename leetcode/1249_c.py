# V1: getting the logic down
# def minRemoveToMakeValid(s: str) -> str:
#     l, r = [], []
#     for idx, char in enumerate(s):
#         if char == "(":
#             l.append(idx)
#         elif char == ")":
#             r.append(idx)

#     for lp in l[::-1]:
#         for rp in r:
#             if lp < rp:
#                 l.remove(lp)
#                 r.remove(rp)
#                 break

#     idx_to_remove = l + r
#     if idx_to_remove is None:
#         new_s = s
#     else:
#         new_s = ""
#         for idx, char in enumerate(s):
#             if not idx in idx_to_remove:
#                 new_s += char

#     return new_s

# V2: using a stack
def minRemoveToMakeValid(s: str) -> str:
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
    actual_output = minRemoveToMakeValid(input)
    print(actual_output)
    print(expected_output)
    assert actual_output == expected_output
