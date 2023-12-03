import argparse
import re
from typing import TypedDict

DEFAULT_INPUT = "2023/day_2/input.txt"
MAX_NUM_CUBES = {"red": 12, "green": 13, "blue": 14}


class CubeSet(TypedDict):
    blue: int
    green: int
    red: int


def main():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-i", "--input", help="input file path")
    args = argParser.parse_args()

    input = args.input if args.input else DEFAULT_INPUT

    sum_game_min_set_power = 0

    with open(input) as f:
        lines = f.readlines()
        for line in lines:
            cube_set_strings = get_cube_set_strings(strip_game_and_id(line))
            game_min_set_power = get_game_min_set_power(cube_set_strings)
            sum_game_min_set_power += game_min_set_power
            print(f"Game min set power is {game_min_set_power}.")

    print(f"Result: {sum_game_min_set_power}")


def get_game_min_set_power(cube_set_strings: list[str]) -> int:
    min_red, min_green, min_blue = 0, 0, 0
    for cube_set_string in cube_set_strings:
        cube_set = get_cube_set(cube_set_string)
        min_red = max(min_red, cube_set["red"])
        min_green = max(min_green, cube_set["green"])
        min_blue = max(min_blue, cube_set["blue"])
    return min_red * min_green * min_blue


def strip_game_and_id(line: str) -> str:
    colon_index = line.find(":")
    assert colon_index != -1
    first_cube_set_index = colon_index + 2
    return line[first_cube_set_index:]


def get_cube_set_strings(line: str) -> list[str]:
    return line.split("; ")


def get_cube_set(cube_set_string: str) -> CubeSet:
    num_red = re.search(r"(\d+) red", cube_set_string)
    num_green = re.search(r"(\d+) green", cube_set_string)
    num_blue = re.search(r"(\d+) blue", cube_set_string)

    cube_set = CubeSet(
        red=int(num_red.group(1)) if num_red is not None else 0,
        green=int(num_green.group(1)) if num_green is not None else 0,
        blue=int(num_blue.group(1)) if num_blue is not None else 0,
    )

    return cube_set


if __name__ == "__main__":
    main()
