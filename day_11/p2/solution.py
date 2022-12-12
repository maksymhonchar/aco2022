from dataclasses import dataclass, field
from typing import Callable, List, Tuple

import numpy as np


@dataclass
class Monkey:
    inspected_counter: int = 0
    items: List[int] = field(
        default_factory=lambda: list()
    )
    operation: Callable[[int], int] = \
        lambda value: value
    test: Callable[[int], int] = \
        lambda value: value
    test_divisible_by: int = 0

    def parse(
        self,
        monkey_str: str
    ) -> None:
        monkey_lines = monkey_str.split('\n')
        # parse 'starting items' line
        items_line = monkey_lines[1].strip()
        self.items = [
            int(item)
            for item in items_line[len('Starting items: '):].split(', ')
        ]
        # parse 'operation' line
        operation_line = monkey_lines[2].strip()
        operation_str = operation_line[len('Operation: new = '):]
        self.operation = lambda old: eval(operation_str, {'old': old})
        # parse 'test' lines
        test_divisible_by_line = monkey_lines[3].strip()
        test_divisible_by_value = int(
            test_divisible_by_line[len('Test: divisible by '):]
        )
        self.test_divisible_by = test_divisible_by_value
        test_if_true_line = monkey_lines[4].strip()
        test_if_true_value = int(
            test_if_true_line[len('If true: throw to monkey '):]
        )
        test_if_false_line = monkey_lines[5].strip()
        test_if_false_value = int(
            test_if_false_line[len('If false: throw to monkey '):]
        )
        self.test = lambda value: (
            test_if_true_value if value % test_divisible_by_value == 0
            else test_if_false_value
        )

    def inspect(
        self,
        global_common_divisor: int
    ) -> Tuple[int, int]:
        self.inspected_counter += 1
        item = self.throw()
        worry_level = self.operation(item)
        new_worry_level = worry_level % global_common_divisor
        recipient = self.test(new_worry_level)
        return recipient, new_worry_level

    def throw(
        self
    ) -> int:
        item_index_to_throw = 0
        return self.items.pop(item_index_to_throw)

    def catch(
        self,
        item: int
    ) -> None:
        self.items.append(item)


def solution(
    input_file_path: str
) -> int:
    monkeys: List[Monkey] = []

    with open(input_file_path) as fs_r:
        monkeys_str = fs_r.read()
        monkeys_separator = '\n\n'
        for monkey_str in monkeys_str.split(monkeys_separator):
            monkey = Monkey()
            monkey.parse(monkey_str)
            monkeys.append(monkey)

    # LCM idea: https://github.com/derivz/AoC2022/blob/master/day9/solution.py
    common_divisor = int(
        np.lcm.reduce(
            [
                monkey.test_divisible_by
                for monkey in monkeys
            ]
        )
    )

    n_rounds = 10_000 + 1
    for round in range(1, n_rounds):
        if round % 1000 == 0:
            monkey_counters = [monkey.inspected_counter for monkey in monkeys]
            print(f'{round=} {monkey_counters=}')

        for monkey in monkeys:
            while monkey.items:
                recipient, new_worry_level = monkey.inspect(common_divisor)
                monkeys[recipient].catch(new_worry_level)

    most_active_monkeys = sorted(
        monkeys,
        key=lambda monkey: monkey.inspected_counter,
    )
    return (
        most_active_monkeys[-1].inspected_counter *
        most_active_monkeys[-2].inspected_counter
    )
