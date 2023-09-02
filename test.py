import unittest
from main import Board, Player


class TestBoardMethods(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    # test for initial board state
    def test_initial_board_state(self):
        expected_board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
        self.assertEqual(self.board.board, expected_board)

    # test for fixing a spot
    def test_fix_spot(self):
        self.board.fix_spot(0, 0, "X")
        self.assertEqual(self.board.board[0][0], "X")

    def test_is_spot_empty(self):
        self.assertTrue(self.board.is_spot_empty(0, 0))
        self.board.fix_spot(0, 0, "X")
        self.assertFalse(self.board.is_spot_empty(0, 0))

    def test_is_winner(self):
        # Setting up a winning state for 'X' across the top row
        for i in range(3):
            self.board.fix_spot(0, i, "X")
        self.assertTrue(self.board.is_winner("X"))

    def test_board_full(self):
        for i in range(3):
            for j in range(3):
                self.board.fix_spot(i, j, "X")
        self.assertTrue(self.board.is_draw())


class TestPlayerMethods(unittest.TestCase):
    def setUp(self):
        self.player = Player("X")

    def test_player_symbol(self):
        self.assertEqual(self.player.symbol, "X")


if __name__ == "__main__":
    unittest.main()
