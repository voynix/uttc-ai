
import ai

from state import *
from util import *

logging.basicConfig(level=logging.INFO)

current_board = Board(X, WILDCARD_MOVE, [])
current_board.create_sub_boards()

moves = current_board.get_moves()
logging.info('AI considering %i moves: %r', len(moves), moves)
ai.explore_state(current_board)
current_board.last_move = WILDCARD_MOVE
ai.explore_state(current_board)
current_board.last_move = WILDCARD_MOVE
ai.explore_state(current_board)
current_board.last_move = WILDCARD_MOVE
ai.explore_state(current_board)
current_board.last_move = WILDCARD_MOVE
ai.explore_state(current_board)
current_board.last_move = WILDCARD_MOVE
ai.explore_state(current_board)
current_board.last_move = WILDCARD_MOVE
ai.explore_state(current_board)
current_board.last_move = WILDCARD_MOVE
ai.explore_state(current_board)
current_board.last_move = WILDCARD_MOVE
ai.explore_state(current_board)
current_board.last_move = WILDCARD_MOVE
ai.explore_state(current_board)
current_board.last_move = WILDCARD_MOVE
ai.explore_state(current_board)
current_board.last_move = WILDCARD_MOVE
ai.explore_state(current_board)
current_board.last_move = WILDCARD_MOVE
ai.explore_state(current_board)
current_board.last_move = WILDCARD_MOVE
ai.explore_state(current_board)
current_board.last_move = WILDCARD_MOVE
ai.explore_state(current_board)
current_board.last_move = WILDCARD_MOVE
ai.explore_state(current_board)
current_board.last_move = WILDCARD_MOVE
ai.explore_state(current_board)
current_board.last_move = WILDCARD_MOVE
ai.explore_state(current_board)
current_board.last_move = WILDCARD_MOVE
exit(1)