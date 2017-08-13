
import ai

from state import *
from util import *

def run_game():
    current_board = Board(X, WILDCARD_MOVE, [])
    current_board.create_sub_boards()
    print current_board
    while True:
        # get AI move
        moves = current_board.get_moves()
        logging.info('AI considering %i moves: %r', len(moves), moves)
        next_move = ai.explore_state(current_board)
        print 'AI move: %s' % str(next_move)
        # update board and check for victory
        current_board.make_move(next_move)
        if check_victory(current_board):
            return
        # display board
        print current_board
        logging.debug(repr(current_board))
        # prompt human for move
        legal_moves = current_board.get_moves()  # make sure this properly acknowledges wildcards
        while True:
            print 'Legal moves are: %r' % legal_moves
            next_move = input('Enter a move as (sub_board, square): ')
            if next_move in legal_moves:
                break
            else:
                print 'Illegal move'
        # update board and check for victory
        current_board.make_move(next_move)
        if check_victory(current_board):
            return

def check_victory(board):
    victory = board.check_victory()
    logging.debug('Victory achieved by (%s)', victory)
    if victory == X:
        print 'AI wins'
    elif victory == O:
        print 'Human wins'
    if victory == EMPTY:
        if len(board.get_moves()) == 0:
            return 'Draw'
        else:
            return False
    return True


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    run_game()
