def solution(
    input_file_path: str
) -> int:
    priorities_sum = 0

    with open(input_file_path) as fs_r:
        for rucksack in fs_r:
            rucksack_half = len(rucksack) // 2
            shared_item = (
                set(rucksack[:rucksack_half]) & \
                set(rucksack[rucksack_half:])
            ).pop()

            priority_correction = \
                1 - ord('a') if str.islower(shared_item) \
                else 27 - ord('A')
            shared_item_priority = ord(shared_item) + priority_correction

            priorities_sum += shared_item_priority

    return priorities_sum 
