import logging

from util import *

class SubBoard(object):
    def __init__(self, position, won=False, won_by=EMPTY):
        self.position = position
        self.board = list(EMPTY * 9)
        self.won = won
        self.won_by = won_by

    def __repr__(self):
        return 'Sub-board %i: %r (won: %r, by: %s)' % (self.position, self.board, self.won, self.won_by)

    def make_copy(self):
        # logging.debug('Sub-board copying self')
        new_sub_board = SubBoard(self.position, self.won, self.won_by)
        new_sub_board.board = list(self.board)  # works as a deep-copy because list members are strings!
        return new_sub_board

    def get_rows(self):
        return [''.join(self.board[:3]), ''.join(self.board[3:6]), ''.join(self.board[6:])]

    def get_moves(self):
        # logging.debug('Finding sub-board moves for sub-board %i', self.position)
        moves = []
        for pos, square in enumerate(self.board):
            if square == EMPTY:
                moves.append((self.position, pos))
        return moves

    def make_move(self, position, player):
        # logging.debug('%s makes sub-board move %r on sub-board %i', player, position, self.position)
        self.board[position] = player
        # check if the sub_board was won by this move
        self.won = True
        self.won_by = player
        if position == 0:
            if self.board[1] == self.board[2] == player:
                return
            elif self.board[3] == self.board[6] == player:
                return
            elif self.board[4] == self.board[8] == player:
                return
        elif position == 1:
            if self.board[0] == self.board[2] == player:
                return
            elif self.board[4] == self.board[7] == player:
                return
        elif position == 2:
            if self.board[0] == self.board[1] == player:
                return
            elif self.board[5] == self.board[8] == player:
                return
            elif self.board[4] == self.board[6] == player:
                return
        elif position == 3:
            if self.board[4] == self.board[5] == player:
                return
            elif self.board[0] == self.board[6] == player:
                return
        elif position == 4:
            if self.board[3] == self.board[5] == player:
                return
            elif self.board[1] == self.board[7] == player:
                return
            elif self.board[0] == self.board[8] == player:
                return
            elif self.board[2] == self.board[6] == player:
                return
        elif position == 5:
            if self.board[3] == self.board[4] == player:
                return
            elif self.board[2] == self.board[8] == player:
                return
        elif position == 6:
            if self.board[7] == self.board[8] == player:
                return
            elif self.board[0] == self.board[3] == player:
                return
            elif self.board[2] == self.board[4] == player:
                return
        elif position == 7:
            if self.board[6] == self.board[8] == player:
                return
            elif self.board[1] == self.board[4] == player:
                return
        elif position == 8:
            if self.board[6] == self.board[7] == player:
                return
            elif self.board[2] == self.board[5] == player:
                return
            elif self.board[0] == self.board[4] == player:
                return
        # the current move didn't win
        # logging.debug('This move did not win the sub-board')
        self.won = False
        self.won_by = EMPTY

    def heuristic_eval(self):
        # logging.debug('Performing heuristic evaluation of sub-board %i' % self.position)
        if self.won:
            value = SUB_BOARD_VICTORY_VALUE[self.won_by]
        else:
            value = SUB_BOARD_VALUES[tuple(self.board)]
        # logging.debug('Sub-board evaluation is %i' % value)
        return value


class Board(object):
    # last_move is the sub_board square in which the last move was played
    # ie which sub_board is eligible for moves on this board
    def __init__(self, active_player, last_move):
        self.active_player = active_player
        self.sub_boards = []
        self.last_move = last_move

    def __repr__(self):
        return 'Board (active_player: %s, last_move: %i) with sub_boards %r' % (self.active_player,
                                                                                self.last_move,
                                                                                self.sub_boards)

    def __str__(self):
        line = '+---+---+---+\n'
        row_line = '+%s|%s|%s+\n'
        rows = dict()
        for index, sub_board in enumerate(self.sub_boards):
            rows[index] = sub_board.get_rows()
        output = line
        for i in xrange(0, 3):
            index = i * 3
            for j in xrange(0, 3):
                output += row_line % (rows[index][j], rows[index+1][j], rows[index+2][j])
            output += line
        return output

    def create_sub_boards(self):
        logging.debug('Creating sub-boards')
        for i in xrange(0, 9):
            self.sub_boards.append(SubBoard(i))

    def make_copy_with_move(self, position):
        # logging.debug('Board copying self with move %r', position)
        new_board = Board(self.active_player, self.last_move)
        new_board.sub_boards = []
        for sub_board in self.sub_boards:
            new_board.sub_boards.append(sub_board.make_copy())
        new_board.make_move(position)
        return new_board

    def get_moves(self):
        # logging.debug('Finding board moves')
        if self.last_move == WILDCARD_MOVE or self.sub_boards[self.last_move].won:  # wildcard
            # logging.debug('Move is wildcard, searching all unclaimed sub-boards')
            moves = []
            for sub_board in self.sub_boards:
                if not sub_board.won:
                    moves.append(sub_board.get_moves())
            # flatten list and return
            return [move for sublist in moves for move in sublist]
        else:
            return self.sub_boards[self.last_move].get_moves()

    def make_move(self, position):
        # logging.debug('%s makes move %r', self.active_player, position)
        sub_board, square = position
        self.sub_boards[sub_board].make_move(square, self.active_player)
        self.active_player = O if self.active_player == X else X
        self.last_move = square

    def check_victory(self):
        # logging.debug('Checking for victory')
        if self.sub_boards[1].won:
            if self.sub_boards[0].won and self.sub_boards[2].won:
                if self.sub_boards[0].won_by == self.sub_boards[1].won_by == self.sub_boards[2].won_by:
                    return self.sub_boards[1].won_by
        if self.sub_boards[3].won:
            if self.sub_boards[0].won and self.sub_boards[6].won:
                if self.sub_boards[0].won_by == self.sub_boards[3].won_by == self.sub_boards[6].won_by:
                    return self.sub_boards[3].won_by
        if self.sub_boards[4].won:
            if self.sub_boards[3].won and self.sub_boards[5].won:
                if self.sub_boards[3].won_by == self.sub_boards[4].won_by == self.sub_boards[5].won_by:
                    return self.sub_boards[4].won_by
            if self.sub_boards[1].won and self.sub_boards[7].won:
                if self.sub_boards[1].won_by == self.sub_boards[4].won_by == self.sub_boards[7].won_by:
                    return self.sub_boards[4].won_by
            if self.sub_boards[0].won and self.sub_boards[8].won:
                if self.sub_boards[0].won_by == self.sub_boards[4].won_by == self.sub_boards[8].won_by:
                    return self.sub_boards[4].won_by
            if self.sub_boards[2].won and self.sub_boards[6].won:
                if self.sub_boards[2].won_by == self.sub_boards[4].won_by == self.sub_boards[6].won_by:
                    return self.sub_boards[4].won_by
        if self.sub_boards[5].won:
            if self.sub_boards[2].won and self.sub_boards[8].won:
                if self.sub_boards[2].won_by == self.sub_boards[5].won_by == self.sub_boards[8].won_by:
                    return self.sub_boards[5].won_by
        if self.sub_boards[7].won:
            if self.sub_boards[6].won and self.sub_boards[8].won:
                if self.sub_boards[6].won_by == self.sub_boards[7].won_by == self.sub_boards[8].won_by:
                    return self.sub_boards[7].won_by
        # logging.debug('No victory found')
        return EMPTY

    def heuristic_eval(self):
        # logging.debug('Performing board heuristic evaluation')
        value = 0
        victory = self.check_victory()
        if victory != EMPTY:
            value = BOARD_VICTORY_VALUE[victory]
        else:
            for position, sub_board in enumerate(self.sub_boards):
                value += BOARD_POSITION_VALUE[position] * sub_board.heuristic_eval()
        # logging.debug('Board evaluation is %i' % value)
        return value
