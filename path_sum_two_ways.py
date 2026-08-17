#!/usr/bin/env python3
# Solution to Project Euler #81 (two-way path sum: right and down)

from __future__ import annotations
from typing import List


class PathSumTwoWays:
    def __init__(self, filename: str):
        # Read file as CSV rows
        with open(filename, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]

        self.values: List[List[int]] = []
        for row_idx, line in enumerate(lines, start=1):
            parts = line.split(",")
            row = []
            for part in parts:
                try:
                    row.append(int(part))
                except ValueError:
                    raise ValueError(f"Bad value {part} on line {row_idx}.")
            self.values.append(row)

        self.F: List[List[int]] | None = None
        self.min_sum: int | None = None

        # Uncomment to display the values table
        # self.display_table(self.values)

    def get_min_sum(self) -> int:
        """Dynamic programming using a 2D cost table."""
        n = len(self.values)
        m = len(self.values[0])
        self.F = [[0] * m for _ in range(n)]

        self.F[0][0] = self.values[0][0]
        for col in range(1, m):
            self.F[0][col] = self.F[0][col - 1] + self.values[0][col]

        for row in range(1, n):
            self.F[row][0] = self.F[row - 1][0] + self.values[row][0]
            for col in range(1, m):
                self.F[row][col] = min(self.F[row-1][col], self.F[row][col-1]) + self.values[row][col]
        self.min_sum = self.F[n-1][m-1]

        # Uncomment to display the cost table
        self.display_table(self.F)

        return self.min_sum

    def display_table(self, table: List[List[int]]) -> None:
        """Nicely formatted 2D table display."""
        m = len(table[0])
        n = len(table)

        max_cell_width = self.num_digits(max(m, n, self.get_max(table)))
        max_row_width = self.num_digits(m)

        # header spacing for row labels
        for _ in range(self.num_digits(n)):
            print(" ", end="")

        # column headers
        for col in range(m):
            print(" ", end="")
            cell_len = self.num_digits(col)
            print(" " * (max_cell_width - cell_len) + str(col), end="")
        print()

        # rows
        for row in range(n):
            cell_len = self.num_digits(row)
            print(" " * (max_row_width - cell_len) + str(row), end="")
            for col in range(m):
                cell_len = self.num_digits(table[row][col])
                print(" " * (max_cell_width - cell_len) + f" {table[row][col]}", end="")
            print()

    def get_solution(self) -> List[int]:
        """
        Backtrack over the cost table to recover the values on the min path.
        Call get_min_sum() first to populate self.F.
        """
        if self.F is None or self.min_sum is None:
            raise RuntimeError("Call get_min_sum() before get_solution().")

        solution: List[int] = []
        row = len(self.F) -1
        col = len(self.F[0]) - 1

        while row > 0 and col > 0:
            solution.append(self.values[row][col])
            if self.F[row-1][col] < self.F[col][row-1]:
                row -= 1
            else:
                col -= 1

        while row > 0:
            solution.append(self.values[row][0])
            row -= 1

        while col > 0:
            solution.append(self.values[0][col])
            col -= 1

        solution.append(self.values[0][0])
        solution.reverse()

        # Sanity check
        assert self.get_sum(solution) == self.min_sum
        return solution

    @staticmethod
    def num_digits(num: int) -> int:
        num = abs(num)
        count = 1
        while num >= 10:
            num //= 10
            count += 1
        return count

    @staticmethod
    def get_sum(array: List[int]) -> int:
        return sum(array)

    @staticmethod
    def get_max(table: List[List[int]]) -> int:
        return max(max(row) for row in table)


def main() -> None:
    filename = "matrix.txt"
    try:
        path_sum = PathSumTwoWays(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        raise SystemExit(1)
    except OSError:
        print(f"Error: Cannot read '{filename}'.")
        raise SystemExit(1)
    except ValueError as e:
        print(f"Error: {e}")
        raise SystemExit(1)

    print("Min sum:", path_sum.get_min_sum())
    print("Values: ", path_sum.get_solution())


if __name__ == "__main__":
    main()
