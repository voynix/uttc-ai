
from state import *
from util import *

states_explored = 0

# MINIMAX search with alpha-beta pruning
def explore_state(board, depth=0, alpha=None, beta=None):
    # logging.debug('Exploring state at depth %i' % depth)
    if depth >= MAX_DEPTH:
        # logging.debug('Max depth reached')
        global states_explored
        states_explored += 1
        return board.heuristic_eval()
    elif board.check_victory() != EMPTY:
        # logging.debug('Found victory/loss; terminating line of exploration')
        value = BOARD_VICTORY_VALUE[board.check_victory()]  # this is unlikely to run, so extra cost here is ok
        # devalue victories based on depth, so earlier victories are worth more
        if board.active_player == X:
            value -= depth
        else:  # active_player == O
            value += depth
        return value
    else:
        moves = board.get_moves()
        best_move, best_move_value = None, None
        # TODO: handle what happens if len(board.get_moves()) == 0 ie draw?
        for move in moves:
            # logging.debug('Exploring moves below %r at depth %i', move, depth)
            # add move to board
            board.make_move(move)
            # recurse w/ depth + 1
            move_value = explore_state(board, depth + 1, alpha, beta)
            # undo move
            board.undo_move(move)
            # compare to best
            if best_move is None or board.active_player == X and move_value > best_move_value or board.active_player == O and move_value < best_move_value:
                # logging.debug('Found new best move %r with value %i at depth %i', move, move_value, depth)
                best_move, best_move_value = move, move_value
            # alpha-beta pruning
            if board.active_player == X:
                if beta is not None and best_move_value >= beta:
                    break  # return immediately
                if best_move_value > alpha:
                    alpha = best_move_value
            else:  # active_player == O
                if alpha is not None and best_move_value <= alpha:
                    break  # return immediately
                if best_move_value < beta:
                    beta = best_move_value
            # debug!
            # if depth == 0:
            #     logging.debug('Move %r with value %i', move, move_value)
        # if depth 0, return best move
        if depth == 0:
            logging.info('%i states explored', states_explored)
            states_explored = 0
            return best_move
        # otherwise return value of best move
        else:
            # logging.debug('Found new best move %r with value %i at depth %i', best_move, best_move_value, depth)
            return best_move_value
