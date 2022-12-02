def solution(
    input_file_path: str
) -> int:
    moves = {
        'A': 'rock',
        'B': 'paper',
        'C': 'scissors',

        'X': 'loss',
        'Y': 'draw',
        'Z': 'win'
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
    outcome_opponent_perspective = {
        'win': 'loss',
        'draw': 'draw',
        'loss': 'win'
    }

    total_score = 0
    with open(input_file_path) as fs_r:
        move_separator = ' '
        for round in fs_r:
            opponent_move, your_outcome = round.strip().split(move_separator)
            opponent_outcome = outcome_opponent_perspective[moves[your_outcome]]
            your_move = [
                rule_move
                for rule_move, rule_outcome
                in rules[moves[opponent_move]].items()
                if rule_outcome == opponent_outcome
            ][0]
            total_score += \
                scores['outcome_score'][moves[your_outcome]] + \
                scores['response_score'][your_move]

    return total_score
