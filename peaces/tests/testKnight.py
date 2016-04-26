import unittest

from peaces.figures import Knight


class TestKnight(unittest.TestCase):

    def setUp(self):
        self.knight = Knight()

    def test_rook_name(self):
        self.assertEquals(self.knight.piece_type, 'N')

    def test_rook_can_move(self):
        knight_moves = self.knight.can_move_to(3, 3, 5, 5)

        expected = [(1, 2),
                    (1, 4),
                    (2, 1),
                    (2, 5),
                    (4, 1),

                    (4, 5),
                    (5, 2),
                    (5, 4),
                    ]
        for expected_position in expected:
            self.assertTrue(expected_position in knight_moves, msg='position not found: (%s, %s) ' % expected_position)

    def test_rook_can_move_first(self):
        rook_moves = self.knight.can_move_to(2, 2, 5, 5)

        expected = [(1, 4),
                    (3, 4),
                    (4, 3),
                    (4, 1),
                    ]
        for expected_position in expected:
            self.assertTrue(expected_position in rook_moves, msg='position not found: (%s, %s) ' % expected_position)

    def test_rook_can_kill(self):
        existing_pieces = [
            (1, 1),
            (2, 1),
            (4, 1),
            (5, 2),
        ]
        self.assertTrue(self.knight.can_kill_piece((3, 3), existing_pieces, 5, 5))

    def test_rook_can_not_kill(self):
        existing_pieces = [
            (1, 1),
            (2, 2),
            (3, 4),
            (4, 2),
            (5, 5),
        ]
        self.assertFalse(self.knight.can_kill_piece((3, 3), existing_pieces, 5, 5))

    def test_rook_can_kill_second(self):
        existing_pieces = [
            (1, 1),
            (5, 3),
            (4, 3),
            (5, 2),
        ]
        self.assertTrue(self.knight.can_kill_piece((2, 2), existing_pieces, 5, 5))