import os
from collections import defaultdict
from typing import DefaultDict, List


def solution(
    input_file_path: str
) -> int:
    dirs_size: DefaultDict[str, int] = defaultdict(int)
    current_dir: List[str] = []
    with open(input_file_path) as fs_r:
        for line in fs_r:
            if line.startswith('$ cd'):
                cd_dir = line[len('$ cd '):].strip()
                if cd_dir == '..':
                    current_dir.pop()
                else:
                    current_dir.append(cd_dir)
            elif str.isnumeric(line[0]):
                file_size = int(line.split(' ')[0])
                for dir_idx in range(len(current_dir)):
                    dir_path = os.sep.join(current_dir[:dir_idx+1])
                    dirs_size[dir_path] += file_size

    dir_size_threshold = 100_000
    return sum(
        [
            value
            for value in dirs_size.values()
            if value <= dir_size_threshold
        ]
    )
