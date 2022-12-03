import string


def solution(
    input_file_path: str
) -> int:
    ascii_letters = string.ascii_lowercase + string.ascii_uppercase
    priorities_sum = 0

    with open(input_file_path) as fs_r:
        for rucksack in fs_r:
            rucksack_half = len(rucksack) // 2
            shared_item = (
                set(rucksack[:rucksack_half]) & \
                set(rucksack[rucksack_half:])
            ).pop()

            priorities_sum += ascii_letters.index(shared_item) + 1

    return priorities_sum 
