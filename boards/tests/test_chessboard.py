import unittest
# noinspection PyDeprecation
from sets import Set

from boards.chess_board import ChessBoard
from pieces.pieces import Rook, King


class TestChessBoard(unittest.TestCase):

    def setUp(self):
        self.m = 3
        self.n = 3
        self.init_board = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.pieces_to_place = [King(), King(), Rook()]
        self.board = ChessBoard(self.m, self.n, [King(), King(), Rook()])

    def test_init(self):

        self.assertEqual(self.board.m_val, self.m)
        self.assertEqual(self.board.n_val, self.n)
        self.assertEqual(len(self.board.pieces_to_place), len(self.pieces_to_place))
        self.assertItemsEqual(self.board.board, self.init_board)
        self.assertEqual(self.board.on_board, [])
        self.assertSetEqual(self.board.solutions, Set())

    def test_reset(self):
        self.board.on_board.append(1)
        self.board.on_board.append(2)
        self.board.reset()
        self.assertItemsEqual(self.board.board, self.init_board)
        self.assertEquals(self.board.on_board, [])

    def test_init_board(self):
        res = self.board.init_board()
        self.assertEqual(res, self.init_board)

    def test_initial_number_of_solutions(self):
        self.assertEqual(self.board.number_of_solutions(), 0)

    def test_number_of_solutions(self):
        self.board.solve()
        self.assertEqual(self.board.number_of_solutions(), 4)
