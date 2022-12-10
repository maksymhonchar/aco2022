from typing import List


def draw_pixel(
    image: List[str],
    cycle: int,
    x: int
) -> None:
    dark_pixel = '.'
    lit_pixel = '#'
    image_width = 40
    # draw pixel
    pixel_idx = cycle % image_width
    if x-1 <= pixel_idx <= x+1:
        image.append(lit_pixel)
    else:
        image.append(dark_pixel)
    # draw new line
    if pixel_idx == (image_width-1):
        image.append('\n')


def solution(
    input_file_path: str
) -> None:
    x = 1
    cycle = 0
    image: List[str] = []

    with open(input_file_path) as fs_r:
        for instruction in fs_r:
            sep = ' '
            args = instruction.strip().split(sep)
            cmd = args[0]
            if cmd == 'noop':
                draw_pixel(image, cycle, x)
                cycle += 1
            elif cmd == 'addx':
                # addx: cycle 1
                draw_pixel(image, cycle, x)
                cycle += 1
                # addx: cycle 2
                draw_pixel(image, cycle, x)
                x += int(args[1])
                cycle += 1

    print(''.join(image))
