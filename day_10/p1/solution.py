from typing import List


def solution(
    input_file_path: str
) -> int:
    x = 1
    log: List[int] = [x]

    with open(input_file_path) as fs_r:
        for instruction in fs_r:
            sep = ' '
            args = instruction.strip().split(sep)
            cmd = args[0]
            if cmd == 'noop':
                log.append(x)
            elif cmd == 'addx':
                log.append(x)
                x += int(args[1])
                log.append(x)

    start_idx = 20
    max_idx = 220
    step_idx = 40
    return sum(
        [
            idx * log[idx - 1]
            for idx in range(start_idx, max_idx + 1, step_idx)
        ]
    )
