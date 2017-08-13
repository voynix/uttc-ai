import re

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
            next_move = get_move()
            if next_move is None:
                continue
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

def get_move():
    move = raw_input('Enter your move or \'help\': ')
    if move == 'help':
        print 'To play on the s-th sub-board in the p-th position, enter any of the following:'
        print '\t(s, p)'
        print '\ts-p'
        print '\tsp'
        print
        print 'Sub-boards and positions are numbered as follows:'
        print '\t+---+'
        print '\t|012|'
        print '\t|345|'
        print '\t|678|'
        print '\t+---+'
        return None
    else:
        if len(move) == 2:  # sp
            s, p = move[0], move[1]
        elif len(move) == 3:  # s-p
            s, p = move.split('-')
        elif re.match(r'\(\d, ?\d\)', move) is not None:  # (s,p) and (s, p)
            parts = move.split(',')
            s = parts[0][-1]
            p = parts[1][-2]
        else:
            print '\'%s\' is not parseable as a move' % move
            return None
        try:
            sub_board = int(s)
            position = int(p)
        except ValueError:
            print s, p
            print '\'%s\' is not parseable as a move' % move
            return None
        return sub_board, position


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    run_game()
