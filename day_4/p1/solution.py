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

            pair_1_overlaps_pair_2 = (min_pair_1 <= min_pair_2) and (max_pair_1 >= max_pair_2)
            pair_2_overlaps_pair_1 = (min_pair_1 >= min_pair_2) and (max_pair_1 <= max_pair_2)
            if pair_1_overlaps_pair_2 or pair_2_overlaps_pair_1:
                assignments += 1
    
    return assignments
