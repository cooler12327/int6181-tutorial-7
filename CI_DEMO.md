# Tutorial 7: Automated tests on pull requests

Repository: https://github.com/cooler12327/int6181-tutorial-7

Pull request: https://github.com/cooler12327/int6181-tutorial-7/pull/1

## Workflow

`.github/workflows/python-tests.yml` checks out the repository, sets up Python 3.12, and runs all three provided test modules:

```sh
python -m unittest discover -s . -p "test_*.py" -v
```

The `pull_request` event runs the tests when a pull request is opened or updated. A push to `main` and a manual dispatch can also trigger the workflow. The Python standard library is sufficient; no third-party Python packages are required.

## Deliberate defect demonstration

Commit `23194534e98e4a85d087f6b3d1a446aefdded24b` deliberately introduced three implementation defects. The provided test files were not edited.

| Module | Injected defect | Observed test failures |
| --- | --- | --- |
| `parking_fee.py` | Changed the hourly rate from 10.0 to 12.0 | `test_multi_day_parking` and `test_valid_fee_calculation` |
| `password_validator.py` | Increased the minimum accepted password length from 8 to 9 | `test_valid_passwords` |
| `triangle.py` | Allowed equality in the triangle inequality check | `test_invalid_triangle_inequalities_return_false` |

The first pull request workflow ran 14 test methods and reported `FAILED (failures=4)` with exit code 1.

Failed run: https://github.com/cooler12327/int6181-tutorial-7/actions/runs/42019210541

## Repair and verification

Restore the hourly rate to 10.0, accept passwords of length 8, and reject a triangle whenever the sum of two sides is less than or equal to the third side. Commit the corrections to the same `ci-bug-demo` branch. The updated pull request must start a new workflow run; its test log should show `Ran 14 tests` and `OK`.

The final implementations are the original correct implementations supplied with the exercise. The deliberate-defect commit and the failed run remain available in the history to demonstrate what CI detected.

This exercise demonstrates continuous integration. It does not configure application deployment.
