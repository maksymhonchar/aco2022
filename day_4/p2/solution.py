def solution(
    input_file_path: str
) -> int:
    pairs_separator = ','
    sections_separator = '-'
    assignments = 0

    with open(input_file_path) as fs_r:
        for assignment_pairs in fs_r:
            min_pair_1, max_pair_1, min_pair_2, max_pair_2 = [
                int(section)
                for pair in assignment_pairs.strip().split(pairs_separator)
                for section in pair.split(sections_separator)
            ]

            ranges_overlap = \
                ((min_pair_1 <= min_pair_2) and (min_pair_2 - max_pair_1 <= 0)) or \
                ((min_pair_1 >= min_pair_2) and (min_pair_1 - max_pair_2 <= 0))
            if ranges_overlap:
                assignments += 1

    return assignments
