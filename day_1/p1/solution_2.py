def solution_2(
    input_file_path: str
) -> int:
    with open(input_file_path) as fs_r:
        elfs_raw_calories = fs_r.read().split('\n\n')
        elfs_calories = [
            sum(
                [int(raw_calorie) for raw_calorie in raw_calories.split('\n')]
            )
            for raw_calories in elfs_raw_calories
        ]
        return max(elfs_calories)
