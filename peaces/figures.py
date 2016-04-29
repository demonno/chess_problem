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
    """Base class for chess pieces"""

    def __init__(self, piece_type):
        """Use for identification of piece"""

        self._piece_type = piece_type
        # Used for sorting pieces
        self.weight = 0

    def __str__(self):
        return self.piece_type

    def __repr__(self):
        return self.piece_type

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
        """Check if piece can kill at least one existing piece. return True."""

    @abstractmethod
    def can_move_to(self, column, row, m, n):
        """Find all coordinates where piece can move. return list of tuples."""

    @staticmethod
    def filter_moves(moves, m, n):
        """Filter moves values surrounded by 0 and m, n. return filtered list."""
        return filter(lambda x: 0 < x[0] <= m and 0 < x[1] <= n, moves)


class King(Piece):
    """class `King` chess piece"""

    def __init__(self):
        super(King, self).__init__('K')
        self.weight = 10

    def can_kill_piece(self, current_position, pieces_on_board, m, n):
        """Check if King can kill at least one piece on board from `current_position`. return True."""
        moves = self.can_move_to(current_position[0], current_position[1], m, n)

        for piece in pieces_on_board:
            if piece in moves:
                return True

        return False

    def can_move_to(self, column, row, m, n):
        """Determine all moves, which King can do, from `column` and `row` square
        parameters `m`, `n` are board information
        according them moves which go out of the board are not included

        :param row: initial row of piece
        :param column: initial column of piece
        :param m: width of the board
        :param n: height of the board
        :return: list of columns and rows where King can move
        """
        moves = [
            (column - 1, row - 1),
            (column - 1, row - 0),
            (column - 1, row + 1),

            (column - 0, row - 1),
            (column - 0, row + 1),

            (column + 1, row - 1),
            (column + 1, row - 0),
            (column + 1, row + 1),
        ]
        moves = self.filter_moves(moves, m, n)
        return moves


class Rook(Piece):
    """class `Rook` chess piece"""

    def __init__(self):
        super(Rook, self).__init__('R')
        self.weight = 40

    def __str__(self):
        return self.piece_type

    def can_kill_piece(self, current_position, pieces_on_board, m, n):
        """Check if `Rook` can kill at least one piece on board from `current_position`. return True."""
        for piece in pieces_on_board:
            if piece[0] == current_position[0] or piece[1] == current_position[1]:
                return True
        return False

    def can_move_to(self, column, row, m, n):
        """Find all possible positions where `Rook` can move from current `column` and `row`. return list of tuples."""
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
    """class `Bishop` chess piece"""

    def __init__(self):
        super(Bishop, self).__init__('B')
        self.weight = 30

    def can_kill_piece(self, current_position, pieces_on_board, m, n):
        """check if `Bishop` can kill at least one piece on board from `current_position` . return True."""
        moves = self.can_move_to(current_position[0], current_position[1], m, n)

        for piece in pieces_on_board:
            if piece in moves:
                return True

        return False

    def can_move_to(self, column, row, m, n):
        """Find all possible positions where `Bishop` can move from current `column` and `row`.

        :param column: current column index of piece
        :param row: current row index of piece
        :param m: width of the board
        :param n: height of the board
        :return: list of tuples.
        """
        moves = []
        m += 1
        for i in xrange(1, m - column):
            moves.append((column + i, row + i))
            moves.append((column + i, row - i))

        for i in xrange(1, column):
            moves.append((column - i, row + i))
            moves.append((column - i, row - i))

        moves = self.filter_moves(moves, m, n)
        return moves


class Knight(Piece):
    """class `Knight` chess piece"""

    def __init__(self):
        super(Knight, self).__init__('N')
        self.weight = 20

    def can_kill_piece(self, current_position, pieces_on_board, m, n):
        """check if `Knight` can kill at least one piece on board from `current_position`. return True."""
        moves = self.can_move_to(current_position[0], current_position[1], m, n)

        for piece in pieces_on_board:
            if piece in moves:
                return True

        return False

    def can_move_to(self, column, row, m, n):
        """Find all possible positions where `Knight` can move from current `column` and `row

        :param column: current column index of piece
        :param row: current row index of piece
        :param m: width of the board
        :param n: height of the board
        :return: list of tuples
        """
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

        moves = self.filter_moves(moves, m, n)
        return moves


class Queen(Rook, Bishop):
    """class `Queen` chess piece"""

    def __init__(self):
        Piece.__init__(self, 'Q')
        Piece.weight = 50

    def can_kill_piece(self, current_position, pieces_on_board, m, n):
        """check if `Queen` can kill at least one piece on board from `current_position`. return True."""
        return Rook.can_kill_piece(self, current_position, pieces_on_board, m, n) \
            or Bishop.can_kill_piece(self, current_position, pieces_on_board, m, n)

    def can_move_to(self, column, row, m, n):
        """Find all possible positions where `Queen` can move from current `column` and `row`. return list of tuples."""
        moves = Rook.can_move_to(self, column, row, m, n)
        moves += Bishop.can_move_to(self, column, row, m, n)
        return moves
