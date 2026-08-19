#!/usr/bin/env python3
"""Unit tests for sqrt.py, converted from the original bash test harness.

Each case runs `python sqrt.py <args>` as a subprocess and checks two things,
in this order (matching the original script):

    1. the process exit code, then
    2. the combined stdout+stderr output.

Output is captured with stderr merged into stdout (the bash `2>&1`), carriage
returns are stripped (`tr -d '\\r'`), and the expected string is compared with a
single trailing newline appended (print() adds exactly one).

Run with either:
    python test_sqrt.py            # unittest runner
    python -m pytest test_sqrt.py  # pytest also works
"""

import os
import subprocess
import sys
import unittest

# Path to the program under test. Override with SQRT_SCRIPT if needed.
SCRIPT = os.environ.get("SQRT_SCRIPT", "sqrt.py")

# (args, expected_output, expected_return_code)
# `args` is a whitespace-separated string; "" means no arguments.
TEST_CASES = [
    ("",                "Usage: python sqrt.py <value> [epsilon]",             1),
    ("10 11 12",        "Usage: python sqrt.py <value> [epsilon]",             1),
    ("ten",             "Error: Value argument must be a double.",             1),
    ("10 x",            "Error: Epsilon argument must be a positive double.",  1),
    ("10 0",            "Error: Epsilon argument must be a positive double.",  1),
    ("10 -1",           "Error: Epsilon argument must be a positive double.",  1),
    ("inf",             "inf",                                                 0),
    ("nan",             "nan",                                                 0),
    ("-1.2",            "nan",                                                 0),
    ("-0.4",            "nan",                                                 0),
    ("0",               "0.00000000",                                          0),
    ("1",               "1.00000000",                                          0),
    ("4",               "2.00000000",                                          0),
    ("1048576",         "1024.00000000",                                       0),
    ("10",              "3.16227766",                                          0),
    ("734658345.678",   "27104.58163628",                                      0),
    ("987",             "31.41655614",                                         0),
    ("987 1",           "31.41656137",                                         0),
    ("1051",            "32.41913015",                                         0),
    ("1051 0.5",        "32.41913908",                                         0),
    ("20.0 1",          "4.47831445",                                          0),
    ("20.0 0.01",       "4.47214022",                                          0),
    ("20.2 0.0001",     "4.49444101",                                          0),
    ("0.5 1e-4",        "0.70710678",                                          0),
    ("0.3333333 1e-6",  "0.57735024",                                          0),
]


def setUpModule():
    """Abort early with a clear message if the program is missing."""
    if not os.path.isfile(SCRIPT):
        raise unittest.SkipTest(f"File '{SCRIPT}' not found. Test skipped.")


class SqrtTest(unittest.TestCase):
    _LINE = "_" * 72

    def _run(self, args):
        """Run sqrt.py with the given args; return (output, return_code)."""
        result = subprocess.run(
            [sys.executable, SCRIPT, *args.split()],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,  # merge stderr into stdout, like 2>&1
            text=True,
        )
        output = result.stdout.replace("\r", "")  # like tr -d '\r'
        return output, result.returncode

    def _diff_message(self, expected, received):
        msg = (
            f"\n\nExpected{self._LINE}\n{expected}"
            f"\nReceived{self._LINE}\n{received}\n"
            f"\nExpected length: {len(expected)}, received length: {len(received)}"
        )
        if len(expected) - len(received) == 1:
            msg += "\nPerhaps you are missing the trailing newline character?"
        return msg


def _make_test(args, expected_output, expected_rc):
    def test(self):
        output, rc = self._run(args)
        # Check the exit code first, matching the original script's precedence.
        self.assertEqual(
            rc, expected_rc,
            f"Return value is {rc}, expected {expected_rc}.",
        )
        expected = expected_output + "\n"
        self.assertEqual(output, expected, self._diff_message(expected, output))

    return test


# Attach one test method per case so each is counted and reported separately.
for _i, (_args, _expected, _rc) in enumerate(TEST_CASES, start=1):
    _method = _make_test(_args, _expected, _rc)
    _method.__doc__ = f"sqrt.py {(_args or '(no args)')!r} -> exit {_rc}"
    setattr(SqrtTest, f"test_{_i:02d}", _method)

del _i, _args, _expected, _rc, _method


if __name__ == "__main__":
    unittest.main(verbosity=2)