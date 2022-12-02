def solution(
    input_file_path: str
) -> int:
    moves = {
        'A': 'rock',
        'B': 'paper',
        'C': 'scissors',

        'X': 'rock',
        'Y': 'paper',
        'Z': 'scissors'
    }
    rules = {
        'rock': {'rock': 'draw', 'paper': 'loss', 'scissors': 'win'},
        'paper': {'rock': 'win', 'paper': 'draw', 'scissors': 'loss'},
        'scissors': {'rock': 'loss', 'paper': 'win', 'scissors': 'draw'}
    }
    scores = {
        'outcome_score': {
            'loss': 0,
            'draw': 3,
            'win': 6
        },
        'response_score': {
            'rock': 1,
            'paper': 2,
            'scissors': 3
        }
    }

    total_score = 0
    with open(input_file_path) as fs_r:
        move_separator = ' '
        for round in fs_r:
            opponent_move, your_move = round.strip().split(move_separator)
            outcome = rules[moves[your_move]][moves[opponent_move]]
            total_score += \
                scores['outcome_score'][outcome] + \
                scores['response_score'][moves[your_move]]

    return total_score
