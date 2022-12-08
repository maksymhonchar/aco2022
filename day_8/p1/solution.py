def solution(
    input_file_path: str
) -> int:
    n_visible = 0

    with open(input_file_path) as fs_r:
        trees_map = fs_r.read().splitlines()
        trees_map_len = len(trees_map)

    for x_idx in range(1, trees_map_len - 1):
        for y_idx in range(1, trees_map_len - 1):
            tree = trees_map[y_idx][x_idx]
            # oy vision
            tree_vision_top = [
                tree > trees_map[y_idx - (correction+1)][x_idx]
                for correction in range(y_idx)
            ]
            tree_vision_bot = [
                tree > trees_map[y_idx + (correction+1)][x_idx]
                for correction in range(trees_map_len - y_idx - 1)
            ]
            # ox vision
            tree_vision_left = [
                tree > trees_map[y_idx][x_idx - (correction+1)]
                for correction in range(x_idx)
            ]
            tree_vision_right = [
                tree > trees_map[y_idx][x_idx + (correction+1)]
                for correction in range(trees_map_len - x_idx - 1)
            ]
            # is visible flag
            is_visible = (
                all(tree_vision_top) or
                all(tree_vision_bot) or
                all(tree_vision_left) or
                all(tree_vision_right)
            )
            if is_visible:
                n_visible += 1

    n_visible += 4*trees_map_len - 4

    return n_visible
