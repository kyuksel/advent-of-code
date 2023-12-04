import argparse
import re
from typing import TypedDict

DEFAULT_INPUT = "2023/day_3/input.txt"

REGEX_SYMBOL = re.compile("([^.\s\d]+)")
REGEX_NUMBER = re.compile(r"(\d+)")


class Number(TypedDict):
    value: int
    row: int
    start: int
    end: int


def main():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-i", "--input", help="input file path")
    args = argParser.parse_args()

    input = args.input if args.input else DEFAULT_INPUT

    num_columns, num_rows = 140, 140
    # initialize to True meaning number can be placed here
    symbol_adjacency_matrix = [[False] * num_columns for _ in range(num_rows)]

    numbers = []

    with open(input) as f:
        row = -1
        lines = f.readlines()
        for line in lines:
            row += 1
            update_symbol_adjacency_matrix(line, row, symbol_adjacency_matrix)
            numbers += get_numbers(line, row)

    part_numbers = []
    for number in numbers:
        if all(
            symbol_adjacency_matrix[number["row"]][number["start"] : number["end"] + 1]
        ):
            part_numbers.append(number["value"])

    print(f"Part numbers: {part_numbers}")
    result = sum(part_numbers)
    print(f"Result: {result}")


def update_symbol_adjacency_matrix(
    line: str, row: int, symbol_adjacency_matrix: list[list[bool]]
) -> None:
    for match in re.finditer(REGEX_SYMBOL, line):
        column = match.start()
        for r in range(row - 1, row + 1):
            for c in range(column - 1, column + 1):
                symbol_adjacency_matrix[r][
                    c
                ] = True  # a part number can't touch this location


def get_numbers(line: str, row: int) -> list[Number]:
    for match in re.finditer(REGEX_NUMBER, line):
        yield Number(
            value=int(match.group()), row=row, start=match.start(), end=match.end()
        )


if __name__ == "__main__":
    main()
