
from state import *
from util import *

# basic MINIMAX search
def explore_state(board, depth=0):
    logging.debug('Exploring state at depth %i' % depth)
    if depth >= MAX_DEPTH:
        logging.debug('Max depth reached')
        return board.heuristic_eval()
    else:
        moves = board.get_moves()
        best_move, best_move_value = None, None
        for move in moves:
            logging.debug('Exploring moves below %r at depth %i', move, depth)
            # make new board with move
            new_board = board.make_copy_with_move(move)
            # recurse w/ depth + 1
            move_value = explore_state(new_board, depth + 1)
            # compare to best
            if best_move is None or board.active_player == X and move_value > best_move_value or board.active_player == O and move_value < best_move_value:
                logging.debug('Found new best move %r with value %i at depth %i', move, move_value, depth)
                best_move, best_move_value = move, move_value
            # debug!
            if depth == 0:
                logging.debug('Move %r with value %i', move, move_value)
        # if depth 0, return best move
        if depth == 0:
            return best_move
        # otherwise return value of best move
        else:
            logging.debug('Found new best move %r with value %i at depth %i', best_move, best_move_value, depth)
            return best_move_value
