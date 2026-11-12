"""Regression tests for the Lecture 10 tic-tac-toe review exercise."""
import contextlib
import io
import unittest
from unittest.mock import patch

import game


class GameReviewTests(unittest.TestCase):
    X_WIN = ["1 1", "2 1", "1 2", "2 2", "1 3"]
    O_WIN = ["1 1", "2 1", "1 2", "2 2", "3 3", "2 3"]
    NINTH_WIN = ["1 1", "1 2", "1 3", "2 1", "2 2", "2 3", "3 2", "3 1", "3 3"]
    DRAW = ["1 1", "1 2", "1 3", "2 2", "2 1", "2 3", "3 2", "3 1", "3 3"]

    def play(self, moves):
        output = io.StringIO()
        with patch("builtins.input", side_effect=moves), contextlib.redirect_stdout(output):
            game.main()
        return output.getvalue()

    def test_empty_board_is_not_a_win(self):
        self.assertFalse(game.is_win([[" "] * 3 for _ in range(3)]))

    def test_all_eight_winning_lines_for_both_players(self):
        lines = [[(r, c) for c in range(3)] for r in range(3)]
        lines += [[(r, c) for r in range(3)] for c in range(3)]
        lines += [[(i, i) for i in range(3)], [(i, 2 - i) for i in range(3)]]
        for marker in ("X", "O"):
            for line in lines:
                with self.subTest(marker=marker, line=line):
                    board = [[" "] * 3 for _ in range(3)]
                    for row, column in line:
                        board[row][column] = marker
                    self.assertTrue(game.is_win(board))

    def test_mixed_lines_are_not_a_win(self):
        self.assertFalse(game.is_win([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]))

    def test_player_one_can_win_using_coordinates_one_to_three(self):
        output = self.play(self.X_WIN)
        self.assertEqual(output.count("Win!"), 1)
        self.assertNotIn("Tie!", output)
        self.assertEqual(output.splitlines()[-3], "X X X")

    def test_player_two_can_win(self):
        output = self.play(self.O_WIN)
        self.assertEqual(output.count("Win!"), 1)
        self.assertNotIn("Tie!", output)
        self.assertEqual(output.splitlines()[-2], "O O O")

    def test_ninth_move_win_is_not_also_reported_as_a_draw(self):
        output = self.play(self.NINTH_WIN)
        self.assertEqual(output.count("Win!"), 1)
        self.assertNotIn("Tie!", output)

    def test_full_board_without_a_winner_is_a_draw(self):
        output = self.play(self.DRAW)
        self.assertEqual(output.count("Tie!"), 1)
        self.assertNotIn("Win!", output)

    def test_occupied_cell_is_rejected_without_losing_the_turn(self):
        output = self.play(["1 1", "1 1", "2 1", "1 2", "2 2", "1 3"])
        self.assertIn("already occupied", output)
        self.assertEqual(output.count("Player 2:"), 3)
        self.assertEqual(output.splitlines()[-3], "X X X")

    def test_non_integer_input_is_rejected_without_crashing(self):
        output = self.play(["hello world", "1.5 2"] + self.X_WIN)
        self.assertEqual(output.count("Enter exactly two integers"), 2)
        self.assertIn("Win!", output)

    def test_wrong_number_of_coordinates_is_rejected(self):
        output = self.play(["", "1", "1 2 3"] + self.X_WIN)
        self.assertEqual(output.count("Enter exactly two integers"), 3)
        self.assertIn("Win!", output)

    def test_zero_negative_and_large_coordinates_are_rejected(self):
        bad = ["0 1", "-1 2", "4 1", "1 0", "1 -2", "1 4"]
        output = self.play(bad + self.X_WIN)
        self.assertEqual(output.count("Coordinates must be between 1 and 3"), 6)
        self.assertEqual(output.splitlines()[-3], "X X X")

    def test_whitespace_between_coordinates_is_allowed(self):
        output = self.play(["  1\t1  "] + self.X_WIN[1:])
        self.assertIn("Win!", output)

    def test_players_alternate_after_successful_moves(self):
        output = self.play(self.X_WIN)
        self.assertEqual(output.count("Player 1:"), 3)
        self.assertEqual(output.count("Player 2:"), 2)

    def test_the_three_final_board_rows_are_printed(self):
        output = self.play(self.DRAW)
        self.assertEqual(output.splitlines()[-3:], ["X O X", "X O O", "O X X"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
