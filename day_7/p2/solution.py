import os
from collections import defaultdict
from typing import DefaultDict, Dict, Optional


def solution(
    input_file_path: str
) -> Optional[int]:
    files_size: Dict[str, int] = {}
    dirs_size: DefaultDict[str, int] = defaultdict(int)
    current_dir = []
    with open(input_file_path) as fs_r:
        for line in fs_r:
            if line.startswith('$ cd'):
                cd_dir = line[len('$ cd '):].strip()
                if cd_dir == '/':
                    current_dir.append('root')
                elif cd_dir == '..':
                    current_dir.pop()
                else:
                    current_dir.append(cd_dir)
            elif str.isnumeric(line[0]):
                size, name = line.strip().split(' ')
                file_path = os.sep.join(current_dir + [name])
                files_size[file_path] = int(size)
                for parent_dir_idx in range(len(current_dir)):
                    parent_dir_path = os.sep.join(
                        current_dir[:parent_dir_idx+1]
                    )
                    dirs_size[parent_dir_path] += files_size[file_path]

    max_disk_size = 70_000_000
    goal_disk_size = 30_000_000
    unused_space = max_disk_size - dirs_size['root']
    space_needed = goal_disk_size - unused_space
    for folder_size in sorted(dirs_size.values()):
        if folder_size >= space_needed:
            return folder_size

    return None
