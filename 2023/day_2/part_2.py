def main():
    sum = 0

    with open("./input.txt") as f:
        # with open("./part_2_test_input_2.txt") as f:
        lines = f.readlines()
        for line in lines:
            line_result = get_sum_of_first_and_last_digits(line)
            # print(f"{line} -> {line_result}")
            sum += line_result

    print(f"Result: {sum}")


def get_sum_of_first_and_last_digits(line: str) -> int:
    first_digit, last_digit = None, None
    word = ""
    for c in line:
        # print(f"Processing char '{c}'")
        word += c
        if c.isdigit():
            if first_digit is None:
                first_digit = int(c)
            else:
                last_digit = int(c)

            word = ""
        else:
            maybe_digit = get_spelled_digit(word)
            if maybe_digit is not None:
                # print(f"maybe_digit -> {maybe_digit}")
                if first_digit is None:
                    first_digit = maybe_digit
                else:
                    last_digit = maybe_digit
            if len(word) == 7:
                word = word[1:]  # Remove first character
        # print(f"\tfirst_digit -> {first_digit}")
        # print(f"\tlast_digit -> {last_digit}")
    if last_digit is None:
        last_digit = first_digit

    assert first_digit is not None and last_digit is not None

    return 10 * first_digit + last_digit


def get_spelled_digit(word: str) -> int | None:
    # print(f"\tword -> {word}")
    last_5_chars = word[-5:]

    if "one" in last_5_chars:
        return 1
    elif "two" in last_5_chars:
        return 2
    elif "three" in last_5_chars:
        return 3
    elif "four" in last_5_chars:
        return 4
    elif "five" in last_5_chars:
        return 5
    elif "six" in last_5_chars:
        return 6
    elif "seven" in last_5_chars:
        return 7
    elif "eight" in last_5_chars:
        return 8
    elif "nine" in last_5_chars:
        return 9
    else:
        return None


if __name__ == "__main__":
    main()
