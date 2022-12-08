from typing import List


def get_vision(
    value: str,
    seq: List[str]
) -> int:
    vision = 0
    while seq:
        if seq[0] >= value:
            vision += 1
            break
        else:
            vision += 1
            seq = seq[1:]
    return vision


def solution(
    input_file_path: str
) -> int:
    scores: List[int] = []

    with open(input_file_path) as fs_r:
        trees_map = fs_r.read().splitlines()
        trees_map_len = len(trees_map)

    for x_idx in range(1, trees_map_len - 1):
        for y_idx in range(1, trees_map_len - 1):
            tree = trees_map[y_idx][x_idx]
            # oy vision
            vision_top = get_vision(
                tree,
                [
                    trees_map[y_idx - (correction+1)][x_idx]
                    for correction in range(y_idx)
                ]
            )
            vision_bot = get_vision(
                tree,
                [
                    trees_map[y_idx + (correction+1)][x_idx]
                    for correction in range(trees_map_len - y_idx - 1)
                ]
            )
            # ox vision
            vision_left = get_vision(
                tree,
                [
                    trees_map[y_idx][x_idx - (correction+1)]
                    for correction in range(x_idx)
                ]
            )
            vision_right = get_vision(
                tree,
                [
                    trees_map[y_idx][x_idx + (correction+1)]
                    for correction in range(trees_map_len - x_idx - 1)
                ]
            )

            score = (
                vision_top *
                vision_bot *
                vision_left *
                vision_right
            )
            scores.append(score)

    return max(scores)
