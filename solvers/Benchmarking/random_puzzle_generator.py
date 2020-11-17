import random


def generate_random_board(m, n, number_of_moves):
    board = []
    for x in range(m):
        for y in range(n):
            board.append((x, y))
    items = ""
    random_possible_action = 0
    last_move = 'x'
    for moves in range(number_of_moves):
        if moves != 0:
            last_move = items[random_possible_action]
        empty_position = board.index((0, 0))

        items = generate_items_string(empty_position, m, n)
        random_possible_action = random.randint(0, len(items) - 1)
        while last_move == items[random_possible_action]:
            random_possible_action = random.randint(0, len(items) - 1)
        if items[random_possible_action] == 'b':
            move_down(board, empty_position, n)
        elif items[random_possible_action] == 'h':
            move_up(board, empty_position, n)
        elif items[random_possible_action] == 'g':
            move_left(board, empty_position)
        else:
            move_right(board, empty_position)

    return board


def generate_items_string(empty_position, m, n):
    items = ""
    if empty_position in range(n):
        items += 'b'
    elif empty_position in range(m * n - n, m * n):
        items += 'h'
    else:
        items += 'hb'

    if empty_position % n == 0:
        items += 'd'
    elif empty_position % n == n - 1:
        items += 'g'
    else:
        items += 'gd'
    return items


def move_right(board: [], empty_position):
    board[empty_position] = board[empty_position + 1]
    board[empty_position + 1] = (0, 0)


def move_left(board: [], empty_position):
    empty_position = board.index((0, 0))
    board[empty_position] = board[empty_position - 1]
    board[empty_position - 1] = (0, 0)


def move_up(board: [], empty_position, n):
    empty_position = board.index((0, 0))
    board[empty_position] = board[empty_position - n]
    board[empty_position - n] = (0, 0)


def move_down(board: [], empty_position, n):
    empty_position = board.index((0, 0))
    board[empty_position] = board[empty_position + n]
    board[empty_position + n] = (0, 0)
