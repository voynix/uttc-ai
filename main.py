
from state import *
from util import *

def run_game():
    current_board = Board(0, X, WILDCARD_MOVE)
    current_board.create_sub_boards()
    print current_board
    while True:
        # get AI move
        moves = current_board.get_moves()
        print moves
        next_move = moves[3 % len(moves)]
        # update board and check for victory
        current_board.make_move(next_move)
        if check_victory(current_board):
            return
        # display board
        print current_board
        print repr(current_board)
        # prompt human for move
        next_move = input('Enter a move as (sub_board, square): ')
        # update board and check for victory
        current_board.make_move(next_move)
        if check_victory(current_board):
            return

def check_victory(board):
    victory = board.check_victory()
    logging.info('Victory was %s', victory)
    if victory == X:
        print 'AI wins'
    elif victory == O:
        print 'Human wins'
    if victory == EMPTY:
        return False
    return True


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    run_game()
