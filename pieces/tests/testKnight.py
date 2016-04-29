import unittest

from pieces.pieces import Knight


class TestKnight(unittest.TestCase):

    def setUp(self):
        self.knight = Knight()

    def test_knight_init(self):
        self.assertEquals(self.knight.piece_type, 'N')
        self.assertEqual(repr(self.knight), 'N')
        self.assertEquals(self.knight.weight, 20)

    def test_knight_can_move(self):
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
        self.assertEqual(len(expected), len(knight_moves), msg="Number of movements don't match")
        for expected_position in expected:
            self.assertTrue(expected_position in knight_moves, msg='position not found: (%s, %s) ' % expected_position)

    def test_knight_can_move_first(self):
        knight_moves = self.knight.can_move_to(2, 2, 5, 5)

        expected = [(1, 4),
                    (3, 4),
                    (4, 3),
                    (4, 1),
                    ]
        self.assertEqual(len(expected), len(knight_moves), msg="Number of movements don't match")
        for expected_position in expected:
            self.assertTrue(expected_position in knight_moves, msg='position not found: (%s, %s) ' % expected_position)

    def test_knight_can_kill(self):
        existing_pieces = [
            (1, 1),
            (2, 1),
            (4, 1),
            (5, 2),
        ]
        self.assertTrue(self.knight.can_kill_piece((3, 3), existing_pieces, 5, 5))

    def test_knight_can_not_kill(self):
        existing_pieces = [
            (1, 1),
            (2, 2),
            (3, 4),
            (4, 2),
            (5, 5),
        ]
        self.assertEqual(self.knight.can_kill_piece((3, 3), existing_pieces, 5, 5), False)

    def test_knight_can_kill_second(self):
        existing_pieces = [
            (1, 1),
            (5, 3),
            (4, 3),
            (5, 2),
        ]
        self.assertTrue(self.knight.can_kill_piece((2, 2), existing_pieces, 5, 5))
