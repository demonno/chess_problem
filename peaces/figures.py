from abc import abstractmethod

PIECE_TYPES = ['K', 'Q', 'B', 'R', 'k']

PIECES = (
    ('K', 'King'),
    ('Q', 'Queen'),
    ('B', 'Bishop'),
    ('R', 'Rook'),
    ('N', 'Knight')
)


class Piece(object):
    def __init__(self, piece_type):
        self._piece_type = piece_type

    @property
    def piece_type(self):
        """
        return type of piece
        * K - King
        * Q - Queen
        * B - Bishop
        * R - Rook
        * N - Knight
        """
        return self._piece_type

    @abstractmethod
    def can_kill_piece(self, current_position, pieces_on_board, m, n):
        """return True if piece can kill at least one existing piece"""

    @abstractmethod
    def can_move_to(self, column, row, m, n):
        """return list of coordinates where piece can move."""


class King(Piece):

    def __init__(self):
        Piece.__init__(self, 'K')

    def can_kill_piece(self, current_position, pieces_on_board, m, n):
        """
        return `True` if King from `current_position` can kill at least one piece on board.
        :param current_position:
        :param pieces_on_board:
        :param m:
        :param n:
        :return: True or False
        """
        moves = self.can_move_to(current_position[0], current_position[1], m, n)
        
        for piece in pieces_on_board:
            if piece in moves:
                return True

        return False

    def can_move_to(self, column, row, m, n):
        """
        Determine all moves, which King can do, from `column` and `row` square
        parameters `m`, `n` are board information
        according them moves which go out of the board are not included

        :param row:
        :param column:
        :param m: width of the board
        :param n: height of the board
        :return: list of columns and rows where King can move
        """
        moves = [(column - 1, row - 1),
                 (column - 1, row - 0),
                 (column - 1, row + 1),

                 (column - 0, row - 1),
                 (column - 0, row + 1),

                 (column + 1, row - 1),
                 (column + 1, row - 0),
                 (column + 1, row + 1),
                 ]
        moves = filter(lambda x: 0 < x[0] <= m and 0 < x[1] <= n, moves)
        return moves


class Rook(Piece):

    def __init__(self):
        Piece.__init__(self, 'R')

    def can_kill_piece(self, current_position, pieces_on_board, m, n):
        """return `True` if Rook from `current_position` can kill at least one piece on board."""
        for piece in pieces_on_board:
            if piece[0] == current_position[0] or piece[1] == current_position[1]:
                return True
        return False

    def can_move_to(self, column, row, m, n):
        """return list of possible positions where Rook can move from current `column` and `row`."""
        moves = []
        m += 1
        n += 1
        for i in xrange(1, m):
            if i != column:
                moves.append((i, row))
        for i in xrange(1, n):
            if i != row:
                moves.append((column, i))
        return moves


class Bishop(Piece):

    def __init__(self):
        Piece.__init__(self, 'B')

    def can_kill_piece(self, current_position, pieces_on_board, m, n):
        moves = self.can_move_to(current_position[0], current_position[1], m, n)

        for piece in pieces_on_board:
            if piece in moves:
                return True

        return False

    def can_move_to(self, column, row, m, n):
        moves = []
        m += 1
        for i in xrange(1, m - column):
            moves.append((column+i, row+i))
            moves.append((column+i, row-i))

        for i in xrange(1, column):
            moves.append((column-i, row+i))
            moves.append((column-i, row-i))

        # TODO try to reuse it from King Piece or add conditions in if
        moves = filter(lambda x: 0 < x[0] <= m and 0 < x[1] <= n, moves)
        return moves


class Knight(Piece):

    def __init__(self):
        Piece.__init__(self, 'N')

    def can_kill_piece(self, current_position, pieces_on_board, m, n):
        moves = self.can_move_to(current_position[0], current_position[1], m, n)

        for piece in pieces_on_board:
            if piece in moves:
                return True

        return False

    def can_move_to(self, column, row, m, n):
        moves = [
            (column + 2, row + 1),
            (column + 2, row - 1),
            (column - 2, row + 1),
            (column - 2, row - 1),

            (column + 1, row + 2),
            (column - 1, row + 2),
            (column + 1, row - 2),
            (column - 1, row - 2),
        ]
        # TODO try to reuse it from King Piece
        moves = filter(lambda x: 0 < x[0] <= m and 0 < x[1] <= n, moves)
        return moves


class Queen(Rook, Bishop):

    def __init__(self):
        Piece.__init__(self, 'Q')

    def can_kill_piece(self, current_position, pieces_on_board, m, n):
        return Rook.can_kill_piece(self, current_position, pieces_on_board, m, n) \
               or Bishop.can_kill_piece(self, current_position, pieces_on_board, m, n)

    def can_move_to(self, column, row, m, n):
        moves = Rook.can_move_to(self, column, row, m, n)
        moves += Bishop.can_move_to(self, column, row, m, n)
        return moves


