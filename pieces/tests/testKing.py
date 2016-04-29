import unittest

from pieces.pieces import King


class TestKing(unittest.TestCase):
    def setUp(self):
        self.king = King()

    def test_king_init(self):
        self.assertEqual(self.king.piece_type, 'K')
        self.assertEqual(repr(self.king), 'K')
        self.assertEqual(self.king.weight, 10)


    def test_king_can_move(self):
        king_moves = self.king.can_move_to(2, 2, 4, 4)

        expected = [
            (1, 1),
            (1, 2),
            (1, 3),
            (2, 1),
            (2, 3),
            (3, 1),
            (3, 2),
            (3, 3),
        ]

        self.assertEquals(expected, king_moves)

    def test_king_can_move_limit_board(self):
        king_moves = self.king.can_move_to(2, 2, 3, 3)

        expected = [
            (1, 1),
            (1, 2),
            (1, 3),
            (2, 1),
            (2, 3),
            (3, 1),
            (3, 2),
            (3, 3),
        ]

        self.assertEquals(expected, king_moves)

    def test_king_can_move_limit_board_first(self):
        king_moves = self.king.can_move_to(1, 1, 3, 3)

        expected = [
            (1, 2),
            (2, 1),
            (2, 2),
        ]

        self.assertEquals(expected, king_moves)

    def test_king_can_move_limit_board_last(self):
        king_moves = self.king.can_move_to(3, 3, 3, 3)

        expected = [
            (2, 2),
            (2, 3),
            (3, 2),
        ]

        self.assertEquals(expected, king_moves)

    def test_king_can_kill(self):
        pieces = [
            (1, 3),
            (3, 3),
            (2, 2)
        ]
        self.assertTrue(self.king.can_kill_piece((1, 1), pieces, 3, 3))

    def test_king_can_not_kill(self):
        pieces = [
            (1, 3),
            (3, 1),
            (3, 2)
        ]
        self.assertEqual(self.king.can_kill_piece((1, 1), pieces, 3, 3), False)