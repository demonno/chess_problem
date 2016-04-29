import unittest

from pieces.pieces import Rook


class TestRook(unittest.TestCase):
    def setUp(self):
        self.rook = Rook()

    def test_rook_name(self):
        self.assertEquals(self.rook.piece_type, 'R')

    def test_rook_can_move(self):
        rook_moves = self.rook.can_move_to(3, 3, 5, 5)
        expected = [
            (3, 1),
            (3, 2),
            (3, 4),
            (3, 5),

            (1, 3),
            (2, 3),
            (4, 3),
            (5, 3),
        ]
        self.assertEqual(len(expected), len(rook_moves), msg="Number of movements don't match")
        for expected_position in expected:
            self.assertTrue(expected_position in rook_moves, msg='position not found: (%s, %s) ' % expected_position)

    def test_rook_can_move_first(self):
        rook_moves = self.rook.can_move_to(1, 1, 5, 5)
        expected = [
            (1, 2),
            (1, 3),
            (1, 4),
            (1, 5),

            (2, 1),
            (3, 1),
            (4, 1),
            (5, 1),
        ]
        self.assertEqual(len(expected), len(rook_moves), msg="Number of movements don't match")
        for expected_position in expected:
            self.assertTrue(expected_position in rook_moves, msg='position not found: (%s, %s) ' % expected_position)

    def test_rook_can_move_third(self):
        rook_moves = self.rook.can_move_to(2, 4, 5, 5)
        expected = [
            (2, 1), (1, 4),
            (2, 2), (3, 4),
            (2, 3), (4, 4),
            (2, 5), (5, 4)
        ]
        self.assertEqual(len(expected), len(rook_moves), msg="Number of movements don't match")
        for expected_position in expected:
            self.assertTrue(expected_position in rook_moves, msg='position not found: (%s, %s) ' % expected_position)

    def test_rook_can_not_kill(self):
        existing_pieces = [
            (1, 1),
            (2, 1),
            (4, 1),
            (5, 2),
        ]
        self.assertEqual(self.rook.can_kill_piece((3, 3), existing_pieces, 5, 5), False)

    def test_rook_can_kill(self):
        existing_pieces = [
            (1, 1),
            (2, 1),
            (3, 2),
            (4, 1),
            (5, 2),
        ]
        self.assertTrue(self.rook.can_kill_piece((3, 3), existing_pieces, 5, 5))

    def test_rook_can_kill_second(self):
        existing_pieces = [
            (1, 1),
            (2, 1),
            (5, 3),
            (4, 1),
            (5, 2),
        ]
        self.assertTrue(self.rook.can_kill_piece((3, 3), existing_pieces, 5, 5))
