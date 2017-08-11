
X = 'x'
O = 'o'
EMPTY = ' '

WILDCARD_MOVE = -1

MAX_DEPTH = 6

SUB_BOARD_VICTORY_VALUE = {X: 20, O: -20}
# center > corner > side
SUB_BOARD_CENTER_VALUES = {X: 3, O: -3, EMPTY: 0}
SUB_BOARD_CORNER_VALUES = {X: 2, O: -2, EMPTY: 0}
SUB_BOARD_SIDE_VALUES = {X: 1, O: -1, EMPTY: 0}
SUB_BOARD_TOP_BOTTOM_LINE_VALUES = {}
SUB_BOARD_CENTER_LINE_VALUES = {}
SUB_BOARD_VALUES = {}
def generate_sub_board_tables():
    for i in [X, O, EMPTY]:
        for j in [X, O, EMPTY]:
            for k in [X, O, EMPTY]:
                SUB_BOARD_TOP_BOTTOM_LINE_VALUES[(i, j, k)] = SUB_BOARD_CORNER_VALUES[i] + SUB_BOARD_SIDE_VALUES[j] + SUB_BOARD_CORNER_VALUES[k]
                SUB_BOARD_CENTER_LINE_VALUES[(i, j, k)] = SUB_BOARD_SIDE_VALUES[i] + SUB_BOARD_CENTER_VALUES[j] + SUB_BOARD_SIDE_VALUES[k]
    for top_line, top_value in SUB_BOARD_TOP_BOTTOM_LINE_VALUES.items():
        for center_line, center_value in SUB_BOARD_CENTER_LINE_VALUES.items():
            for bottom_line, bottom_value in SUB_BOARD_TOP_BOTTOM_LINE_VALUES.items():
                SUB_BOARD_VALUES[top_line + center_line + bottom_line] = top_value + center_value + bottom_value
generate_sub_board_tables()
BOARD_VICTORY_VALUE = {X: 5000, O: -5000}
BOARD_POSITION_VALUE = [2, 1, 2,
                        1, 4, 1,
                        2, 1, 2]
