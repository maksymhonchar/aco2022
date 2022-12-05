from collections import defaultdict


def parse_stacks(
    stacks_lines: list
) -> dict:
    stack_content_str_len = 3
    separator_str_len = 1
    stack_str_len = stack_content_str_len + separator_str_len
    stacks = defaultdict(list)
    for line in stacks_lines[:-1][::-1]:
        crates = [
            line[char_idx:char_idx+stack_str_len]
            for char_idx in range(0, len(line), stack_str_len)
        ]
        for stack_idx, crate in enumerate(crates):
            if crate.strip() != '':
                formatted_crate = (
                    crate
                    .strip()
                    .replace('[', '')
                    .replace(']', '')
                )
                stacks[stack_idx + 1].append(formatted_crate)
    return stacks


def parse_moves(
    moves_lines: list
) -> list:
    moves = []
    for line in moves_lines:
        line = (
            line
            .strip()
            .replace('move ', '')
            .replace(' from ', ',')
            .replace(' to ', ',')
        )
        moves.append(
            [
                int(value)
                for value in line.split(',')
            ]
        )
    return moves


def move(
    stacks: dict,
    moves: list
) -> None:
    for (move_count, move_from, move_to) in moves:
        stacks[move_to].extend(stacks[move_from][-move_count:])
        stacks[move_from] = stacks[move_from][:-move_count]


def solution(
    input_file_path: str
) -> str:
    with open(input_file_path) as fs_r:
        # read stacks
        stacks_lines = []
        for drawing_line in fs_r:
            if drawing_line == '\n':
                break
            stacks_lines.append(drawing_line)
        # read moves
        moves_lines = []
        for drawing_line in fs_r:
            moves_lines.append(drawing_line)

    stacks = parse_stacks(stacks_lines)
    moves = parse_moves(moves_lines)

    move(stacks, moves)

    crates_on_top = ''.join(
        [
            stacks[stack_idx].pop()
            for stack_idx in sorted(stacks)
        ]
    )

    return crates_on_top
