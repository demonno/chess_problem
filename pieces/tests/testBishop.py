import unittest

from pieces.pieces import Bishop


class TestBishop(unittest.TestCase):
    def setUp(self):
        self.bishop = Bishop()

    def test_bishop_name(self):
        self.assertEquals(self.bishop.piece_type, 'B')

    def test_bishop_can_move(self):
        bishop_moves = self.bishop.can_move_to(3, 3, 5, 5)
        expected = [
            (1, 1),
            (2, 2),
            (4, 4),
            (5, 5),

            (1, 5),
            (2, 4),
            (4, 2),
            (5, 1),
        ]
        self.assertEqual(len(expected), len(bishop_moves), msg="Number of movements don't match")
        for expected_position in expected:
            self.assertTrue(expected_position in bishop_moves, msg='position not found: (%s, %s) ' % expected_position)

    def test_bishop_can_move_first(self):
        bishop_moves = self.bishop.can_move_to(1, 5, 5, 5)

        expected = [
            (2, 4),
            (3, 3),
            (4, 2),
            (5, 1),
        ]
        self.assertEqual(len(expected), len(bishop_moves), msg="Number of movements don't match")
        for expected_position in expected:
            self.assertTrue(expected_position in bishop_moves, msg='position not found: (%s, %s) ' % expected_position)

    def test_bishop_can_move_second(self):
        bishop_moves = self.bishop.can_move_to(2, 2, 5, 5)
        expected = [
            (1, 1),
            (3, 1),
            (1, 3),
            (3, 3),
            (4, 4),
            (5, 5),
        ]
        self.assertEqual(len(expected), len(bishop_moves), msg="Number of movements don't match")
        for expected_position in expected:
            self.assertTrue(expected_position in bishop_moves, msg='position not found: (%s, %s) ' % expected_position)

    def test_bishop_can_move_third(self):
        bishop_moves = self.bishop.can_move_to(4, 3, 5, 5)
        expected = [
            (2, 1),
            (3, 2),
            (5, 4),
            (2, 5),
            (3, 4),
            (5, 2)
        ]
        self.assertEqual(len(expected), len(bishop_moves), msg="Number of movements don't match")
        for expected_position in expected:
            self.assertTrue(expected_position in bishop_moves, msg='position not found: (%s, %s) ' % expected_position)

    def test_bishop_can_not_kill(self):
        existing_pieces = [
            (2, 1),
            (2, 3),
            (5, 4),
            (1, 4),
            (3, 4),
        ]
        self.assertEqual(self.bishop.can_kill_piece((3, 3), existing_pieces, 5, 5), False)

    def test_bishop_can_not_kill_second(self):
        existing_pieces = [
            (2, 1),
            (5, 3),
            (4, 1),
            (5, 2),
            (1, 2),
        ]
        self.assertFalse(self.bishop.can_kill_piece((2, 2), existing_pieces, 5, 5))

    def test_bishop_can_kill(self):
        existing_pieces = [
            (2, 1),
            (2, 3),
            (4, 4),
            (5, 4),
            (1, 4),
            (3, 4),
            (5, 5),
        ]
        self.assertTrue(self.bishop.can_kill_piece((3, 3), existing_pieces, 5, 5))

    def test_bishop_can_kill_second(self):
        existing_pieces = [
            (2, 1),
            (5, 3),
            (4, 1),
            (5, 2),
            (1, 2),
            (3, 1)
        ]
        self.assertTrue(self.bishop.can_kill_piece((2, 2), existing_pieces, 5, 5))
