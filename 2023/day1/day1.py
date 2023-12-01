def main():
    sum = 0

    with open("./input.txt") as f:
        lines = f.readlines()
        for line in lines:
            sum += get_sum_of_first_and_last_digits(line)

    print(f"Result: {sum}")


def get_sum_of_first_and_last_digits(line: str) -> int:
    first_digit, last_digit = None, None
    for c in line:
        if c.isdigit():
            if first_digit is None:
                first_digit = int(c)
            else:
                last_digit = int(c)

    if last_digit is None:
        last_digit = first_digit

    assert first_digit is not None and last_digit is not None

    return 10 * first_digit + last_digit


if __name__ == "__main__":
    main()
