from typing import Generator, Optional


def search(
    datastream: str
) -> Optional[int]:
    marker_len = 4
    for char_idx in range(len(datastream)):
        marker = datastream[char_idx:char_idx+marker_len]
        marker_chars_unique = len(set(marker)) == marker_len
        if marker_chars_unique:
            return char_idx + marker_len
    return None


def solution(
    input_file_path: str
) -> Generator[Optional[int], None, None]:
    with open(input_file_path) as fs_r:
        for datastream in fs_r:
            yield search(datastream)
