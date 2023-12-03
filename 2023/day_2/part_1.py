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

    sum_valid_game_ids = 0

    with open(input) as f:
        lines = f.readlines()
        for line in lines:
            cube_set_strings = get_cube_set_strings(strip_game_and_id(line))
            if has_enough_cubes(cube_set_strings):
                valid_game_id = get_game_id(line)
                sum_valid_game_ids += valid_game_id
                print(f"Game {valid_game_id} is valid.")

    print(f"Result: {sum_valid_game_ids}")


def get_game_id(line: str) -> int:
    pattern = "^Game (\d{1,3}):"
    game_id_search = re.search(pattern, line)
    assert game_id_search is not None
    game_id = game_id_search.group(1)
    return int(game_id)


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


def has_enough_cubes(cube_set_strings: list[str]) -> bool:
    for cube_set_string in cube_set_strings:
        cube_set = get_cube_set(cube_set_string)
        is_enough = (
            cube_set["red"] <= MAX_NUM_CUBES["red"]
            and cube_set["green"] <= MAX_NUM_CUBES["green"]
            and cube_set["blue"] <= MAX_NUM_CUBES["blue"]
        )
        if not is_enough:
            return False
    return True


if __name__ == "__main__":
    main()
