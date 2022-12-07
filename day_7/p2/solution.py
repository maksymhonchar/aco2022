import os
from collections import defaultdict
from typing import DefaultDict, Dict


def solution(
    input_file_path: str
) -> int:
    files: Dict[str, int] = {}
    current_dir = ''
    with open(input_file_path) as fs_r:
        for line in fs_r:
            if line.startswith('$ cd'):
                args_sep = ' '
                cmd = line[len('$ '):].strip()
                _, cd_dir = cmd.split(args_sep)
                if cd_dir == '/':
                    current_dir = 'root'
                elif cd_dir == '..':
                    children = current_dir.split(os.sep)[:-1]
                    current_dir = os.sep.join(children)
                else:
                    current_dir = os.path.join(current_dir, cd_dir)
            elif line.startswith('$ ls'):
                continue
            else:
                if not line.startswith('dir'):
                    size, name = line.strip().split(' ')
                    path = os.path.join(current_dir, name)
                    files[path] = int(size)

    folders_size: DefaultDict[str, int] = defaultdict(int)
    for file_path, file_size in files.items():
        parent_dirs = file_path.split(os.sep)[:-1]
        for parent_idx in range(len(parent_dirs)):
            folder = os.sep.join(parent_dirs[:parent_idx + 1])
            folders_size[folder] += file_size

    max_disk_size = 70_000_000
    goal_disk_size = 30_000_000
    unused_space = max_disk_size - folders_size['root']
    space_needed = goal_disk_size - unused_space
    for folder_size in sorted(folders_size.values()):
        if folder_size >= space_needed:
            return folder_size

    return -1
