def solution(
    input_file_path: str
) -> int:
    max_calories = 0
    elf_calories = 0 
    for calories in open(input_file_path):
        if calories == '\n':
            if elf_calories > max_calories:
                max_calories = elf_calories
            elf_calories = 0
        else:
            elf_calories += int(calories.strip())

    # last elf
    if elf_calories > max_calories:
        max_calories = elf_calories

    return max_calories
