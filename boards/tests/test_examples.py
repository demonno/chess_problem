import unittest

from boards.chess_board import ChessBoard
from pieces.pieces import King, Rook, Knight


def r(param):
    return param.replace(' ', '').replace('\n', '')


class TestExamples(unittest.TestCase):
    def setUp(self):
        self.pieces_for_solution_one = [King(), King(), Rook()]
        self.pieces_for_solution_two = [Knight(), Rook(), Rook(), Knight(), Knight(), Knight()]

    def testSolutionOne(self):
        board = ChessBoard(3, 3, self.pieces_for_solution_one)
        board.solve()

        solution_one = \
            """
            K . .
            . . R
            K . .
            """

        solution_two = \
            """
            . R .
            . . .
            K . K
            """

        solution_three = \
            """
            . . K
            R . .
            . . K
            """

        solution_four = \
            """
            K . K
            . . .
            . R .
            """

        self.assertEqual(r(board.solutions.pop()),
                         r(solution_one))

        self.assertEqual(r(board.solutions.pop()),
                         r(solution_two))

        self.assertEqual(r(board.solutions.pop()),
                         r(solution_three))

        self.assertEqual(r(board.solutions.pop()),
                         r(solution_four))

    # noinspection PyListCreation
    def testSolutionTwo(self):
        board = ChessBoard(4, 4, self.pieces_for_solution_two)
        board.solve()

        expected_solutions = []
        expected_solutions.append(("""
        . . . R
        N . N .
        . R . .
        N . N .
        """))

        expected_solutions.append(("""
        . N . N
        . . R .
        . N . N
        R . . .
        """))
        expected_solutions.append(("""
        . N . N
        R . . .
        . N . N
        . . R .
        """))
        expected_solutions.append(("""
        N . N .
        . . . R
        N . N .
        . R . .
        """))
        expected_solutions.append(("""
        . R . .
        N . N .
        . . . R
        N . N .
        """))
        expected_solutions.append(("""
        R . . .
        . N . N
        . . R .
        . N . N
        """))
        expected_solutions.append(("""
        N . N .
        . R . .
        N . N .
        . . . R
        """))
        expected_solutions.append(("""
        . . R .
        . N . N
        R . . .
        . N . N
        """))

        for i in board.solutions:
            self.assertEqual(r(i), r(expected_solutions.pop(0)))
