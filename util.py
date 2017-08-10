
X = 'x'
O = 'o'
EMPTY = ' '

WILDCARD_MOVE = -1

MAX_DEPTH = 6

SUB_BOARD_VICTORY_VALUE = {X: 20, O: -20}
# center > corner > side
SUB_BOARD_POSITION_VALUE = [{X: 2, O: -2}, {X: 1, O: -1}, {X: 2, O: -2},
                            {X: 1, O: -1}, {X: 3, O: -3}, {X: 1, O: -1},
                            {X: 2, O: -2}, {X: 1, O: -1}, {X: 2, O: -2}]
BOARD_VICTORY_VALUE = {X: 5000, O: -5000}
BOARD_POSITION_VALUE = [2, 1, 2,
                        1, 4, 1,
                        2, 1, 2]
