import string


def solution(
    input_file_path: str
) -> int:
    ascii_letters = string.ascii_lowercase + string.ascii_uppercase
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

            priorities_sum += ascii_letters.index(shared_item) + 1

    return priorities_sum
