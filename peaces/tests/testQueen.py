import unittest

from peaces.figures import Queen


class TestQueen(unittest.TestCase):
    def setUp(self):
        self.queen = Queen()

    def test_queen_name(self):
        self.assertEquals(self.queen.piece_type, 'Q')

    def test_queen_can_move(self):
        queen_moves = self.queen.can_move_to(3, 3, 5, 5)
        expected = [
            (3, 1), (1, 3), (1, 1), (1, 5),
            (3, 2), (2, 3), (2, 3), (2, 4),

            (3, 4), (4, 3), (4, 4), (4, 2),
            (3, 5), (5, 3), (5, 5), (5, 1),
        ]
        for expected_position in expected:
            self.assertTrue(expected_position in queen_moves, msg='position not found: (%s, %s) ' % expected_position)

        self.assertEqual(len(expected), len(queen_moves), msg="Number of movements don't match")

    def test_queen_can_move_first(self):
        queen_moves = self.queen.can_move_to(2, 4, 5, 5)
        expected = [
            (1, 3), (2, 1), (3, 3), (4, 2), (5, 1),
            (1, 4), (2, 2), (3, 4), (4, 4), (5, 4),
            (1, 5), (2, 3), (3, 5),
                    (2, 5),
        ]
        for expected_position in expected:
            self.assertTrue(expected_position in queen_moves, msg='position not found: (%s, %s) ' % expected_position)

        self.assertEqual(len(expected), len(queen_moves), msg="Number of movements don't match")

    def test_queen_can_not_kill(self):
        existing_pieces = [
            (1, 2),
            (2, 1),
            (4, 1),
            (1, 4),
            (5, 4),
            (2, 5),
            (4, 5),
        ]
        self.assertEqual(self.queen.can_kill_piece((3, 3), existing_pieces, 5, 5), False)

    def test_queen_can_not_kill_second(self):
            existing_pieces = [
                (1, 1),
                (1, 2),
                (3, 1),
                (3, 2),
                (4, 1),
                (4, 3),
                (4, 5),
                (5, 2),
                (5, 3),
                (5, 5),
            ]
            self.assertEqual(self.queen.can_kill_piece((2, 4), existing_pieces, 5, 5), False)

    def test_queen_can_kill(self):
        existing_pieces = [
            (1, 1),
            (2, 1),
            (3, 2),
            (4, 1),
            (5, 2),
        ]
        self.assertTrue(self.queen.can_kill_piece((3, 3), existing_pieces, 5, 5))

    def test_queen_can_kill_second(self):
        existing_pieces = [
            (1, 1),
            (2, 1),
            (5, 3),
            (4, 1),
            (5, 2),
        ]
        self.assertTrue(self.queen.can_kill_piece((2, 4), existing_pieces, 5, 5))
