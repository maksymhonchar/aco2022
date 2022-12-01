from solution import solution
from solution_2 import solution_2


def main():
    input_file_path = 'day_1/p1/inputs/problem.in'

    result = solution(input_file_path)
    print(f'{result=}')

    result_2 = solution_2(input_file_path)
    print(f'{result_2=}')

    assert(result == result_2)


if __name__ == '__main__':
    main()
