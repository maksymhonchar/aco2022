import operator

def solution(
    input_file_path: str
) -> int:
    priorities_sum = 0

    with open(input_file_path) as fs_r:
        for rucksack in fs_r:
            group_rucksacks = (
                set(group_rucksack.strip())
                for group_rucksack in (
                    rucksack,
                    fs_r.__next__(),
                    fs_r.__next__()
                )
            )
            shared_item = set.intersection(*group_rucksacks).pop()

            priority_correction = \
                1 - ord('a') if str.islower(shared_item) \
                else 27 - ord('A')
            shared_item_priority = ord(shared_item) + priority_correction

            priorities_sum += shared_item_priority

    return priorities_sum
