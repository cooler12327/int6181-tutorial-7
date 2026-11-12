# Lecture 10 tic-tac-toe code review

Author: Huang Wei  
Course: INT6181 Applied Programming with Python  
Source: the Python code in the comments of Lecture 10 slide 10.

## Scope and participation

This is an AI-assisted review exercise. A human classmate reviewer and a moderator have not yet participated. GitHub Copilot is requested as the cyber reviewer. The record does not claim that a classroom group meeting or human peer approval has occurred.

The original `is_win` implementation is retained. The change focuses on input handling, valid turns and termination in `main`.

## Findings and corrections

| ID | Finding | Correction | Regression evidence |
| --- | --- | --- | --- |
| R1 | The prompt accepts coordinates from 1 to 3, but a Python list requires indices from 0 to 2. | Validate the entered coordinates, then subtract 1 from each. | Both players can complete games using the advertised coordinate range. |
| R2 | Non-integer input or the wrong number of coordinates raises `ValueError`. | Catch `ValueError`, explain the input format and retry the same turn. | Blank input, one or three values, words and decimal input are rejected without ending the game. |
| R3 | Zero and negative indices can select unintended cells, and large indices can raise `IndexError`. | Reject both coordinates unless they are between 1 and 3 before indexing. | Six invalid boundary inputs are rejected. |
| R4 | A player can overwrite an occupied square. Counting input attempts can also end the game before nine valid moves. | Reject occupied cells; count only successful placements and change player only after a valid move. | An occupied-cell attempt keeps the original mark and the same player's turn. |
| R5 | Winning on the ninth move also satisfies the original `n == 8` draw condition. | Check for a win first, then check whether the ninth valid move is a draw. | The ninth-move win prints `Win!` exactly once and never `Tie!`; a true full-board draw prints `Tie!`. |

The original first-player behavior was already correct: the loop toggles the initial flag before displaying Player 1. The revised integer player index improves readability; this is not recorded as a separate turn-order defect.

## Validation

Run from the repository root:

```bash
python -m unittest discover -s . -p "test_*.py" -v
```

`test_game.py` contains 14 test methods. The win-line test checks all eight winning lines for each marker, so the test-method count is not the number of individual input cases. Together with the repository's existing 14 test methods, the corrected code passes 28 local tests. GitHub Actions provides the separate online result for the PR.

The 14 game tests were also run against the original source and the first coordinate-only patch. The original produced 11 errors; the coordinate-only patch produced 2 failures and 3 errors; the complete correction passes all 14. Tests are kept unchanged between these three checks.

## Review procedure

1. Preserve the lecture source on `main` as a baseline.
2. Create `lecture10-code-review` and open a PR with the initial coordinate correction.
3. Request an AI review and inspect the comments.
4. Update the same branch with the complete correction and the regression tests.
5. Verify the checks and merge the PR into `main` after reviewing the result.

The PR history records the actual review and integration status. Human walkthrough, group inspection and moderator sign-off remain separate classroom activities to complete with classmates.
