num2word = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    1000: "onethousand",
}


def n1_2__99():
    n1_2__9 = sum(len(num2word[num]) for num in range(1, 10))
    n10_11__19 = sum(len(num2word[num]) for num in range(10, 20))
    n20_30__90 = sum(len(num2word[num]) for num in range(20, 100, 10))
    n20_21__99 = (
        10 * sum(len(num2word[num]) for num in range(20, 100, 10)) + 8 * n1_2__9
    )
    return n1_2__9 + n10_11__19 + n20_21__99


def n100_101__999():
    n1_2__99_ = n1_2__99()
    n_100_200__900 = sum(len(num2word[num]) + len("hundred") for num in range(1, 10))
    return 100 * n_100_200__900 + 9 * n1_2__99_ + 9 * 99 * len("and")


total_letters_in_n1_2__1000 = n1_2__99() + n100_101__999() + len(num2word[1000])
print(total_letters_in_n1_2__1000)
