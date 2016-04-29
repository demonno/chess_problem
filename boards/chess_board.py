"""
Chess Board

Generates all possible unique solutions
"""

from sets import Set


class ChessBoard(object):
    """Class used for generating solutions"""

    def __init__(self, m, n, pieces_to_place):
        self.m_val = m
        self.n_val = n
        self.board = self.init_board()
        self.pieces_to_place = pieces_to_place
        self.on_board = []
        self.solutions = Set()

    def reset(self):
        """Reset all values like it is new board initialized

        This is needed to prepare board for next solutions
        """
        self.on_board = []
        self.board = self.init_board()

    def init_board(self):
        """Initialize board with two dimensional array. Empty values are 0s."""
        return [[0] * (self.n_val + 1) for _ in range(self.m_val + 1)]

    def solve(self):
        """Solve problem from existing parameters

        1. sort pieces according piece weight in decreasing order
        2. loop over board and try to find new solution from each position
        3. add all found solutions in Set
        4. `reset()` board after each attempt of finding the solution
        """
        self.pieces_to_place.sort(key=lambda p: p.weight, reverse=True)
        for i in xrange(1, self.m_val + 1):
            for j in xrange(1, self.n_val + 1):
                if self.place_pieces(0, i, j):
                    self.solutions.add(str(self))
                else:
                    print "Solution doesn't exist from position (%s, %s)" % (i, j)
                self.reset()

    def place_pieces(self, piece_index, column, row):

        """Recursive function to find solution started from position `column`, `row`

        Loop over all position and check for each of them if it is possible to place piece.
        After placing apply changes on board and call `place_pieces` by next piece index.

        If It is not possible to place all existing pieces call `un_apply_piece_on_board` and
        continue finding next solution.

        If no solution found return False

        :param piece_index: index of piece which is going to place on board.
        :param column: index of column on board.
        :param row: index of row on board.
        :return: True or False.
        """
        if len(self.pieces_to_place) == len(self.on_board):
            return True

        for i in xrange(column, self.m_val + 1):
            for j in xrange(row, self.n_val + 1):

                if self.can_place(self.pieces_to_place[piece_index], i, j):
                    moves = self.apply_piece_on_board(i, j, piece_index)
                    if self.place_pieces(piece_index + 1, 1, 1):
                        return True
                    self.un_apply_piece_on_board(i, j, moves)

        return False

    def apply_piece_on_board(self, i, j, piece_index):
        """Apply changes which are required for next placement

        * assign piece to the board
        * append position information (i, j) in `on_board` list
        * decease value by 1 on positions which means restricting access.
        * return list of restricted moves
        """
        self.board[i][j] = self.pieces_to_place[piece_index]
        self.on_board.append((i, j))
        moves = self.pieces_to_place[piece_index].can_move_to(i, j, self.m_val, self.n_val)
        for move in moves:
            self.board[move[0]][move[1]] -= 1
        return moves

    def un_apply_piece_on_board(self, i, j, moves):
        """Undo everything what `apply_piece_on_board` did

         * remove piece from board, assign 0 to the position i, j
         * increase value by 1 on positions
         * remove position from `on_board` list
        """
        self.board[i][j] = 0
        for move in moves:
            self.board[move[0]][move[1]] += 1
        for positions in self.on_board:
            if positions == (i, j):
                self.on_board.remove(positions)
                break

    def can_place(self, piece, column, row):
        """Check if it is safe to place `piece` on the board.

         * check if piece is already on board
         * check if position is not restricted to place piece
         * check if it is safe to place `piece` on position


         return True is it is safe to place piece on position
        """
        return bool((column, row) not in self.on_board
                    and self.board[column][row] >= 0
                    and not piece.can_kill_piece((column, row),
                                                 self.on_board, self.m_val, self.n_val))

    def number_of_solutions(self):
        """return number of solutions"""
        return len(self.solutions)

    def print_solutions(self, include_quantity=False):
        """Print all existing solutions

            If include_quantity is True start printing number of solutions on first line
        """
        if include_quantity:
            print self.number_of_solutions()

        for solution in self.solutions:
            print solution

    def __str__(self):
        """Representation for printing solution"""
        builder = []
        for column in xrange(1, self.m_val + 1):
            for row in xrange(1, self.n_val + 1):
                if not isinstance(self.board[row][column] and self.board[row][column], int):
                    builder.append(str(self.board[row][column]))
                else:
                    builder.append('.')
                builder.append(' ')
            builder.append('\n')

        return "".join(builder)
