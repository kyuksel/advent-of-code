import re
from typing import TypedDict

max_num_cubes = {"red": 12, "green": 13, "blue": 14}


class CubeSet(TypedDict):
    blue: int
    green: int
    red: int


def main():
    # input = "./input.txt"
    input = "./part_1_test_input_1.txt"

    sum_valid_game_ids = 0

    with open(input) as f:
        lines = f.readlines()
        for line in lines:
            cube_set_strings = get_cube_set_strings(strip_game_and_id(line))
            for cube_set_string in cube_set_strings:
                cube_set = get_cube_set(cube_set_string)
                if not has_enough_cubes(cube_set):
                    break
            sum_valid_game_ids += get_game_id(line)

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

    return CubeSet(
        red=int(num_red.group(1)) if num_red is not None else 0,
        green=int(num_green.group(1)) if num_green is not None else 0,
        blue=int(num_blue.group(1)) if num_blue is not None else 0,
    )


def has_enough_cubes(cube_set: CubeSet) -> bool:
    return (
        cube_set["red"] <= max_num_cubes["red"]
        and cube_set["green"] <= max_num_cubes["green"]
        and cube_set["blue"] <= max_num_cubes["blue"]
    )


if __name__ == "__main__":
    main()
