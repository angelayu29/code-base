# shape_columbia

Python algorithm exercises from Intro to Algorithms in SHAPE 2026, organized by topic. 
Final project: Leetcode problem 994 "Rotting Oranges"

## Contents

### `data_structures/`

- **`MyLinkedList.py`** — a doubly linked list implemented from scratch with deque-style operations: `append`/`appendleft`, `pop`/`popleft`, `get`/`set` (also via `[]`), `rotate(n)`, `is_empty`, `__len__`, `__iter__`. Run directly for a demo.
- **`queue_two_stacks.py`** — a `Queue` built from two `Stack` instances (`enqueue`, `dequeue`, `front`). Reads queries from stdin (HackerRank-style: `1 x` enqueue, `2` dequeue, `3` print front).
- **`recursionpractice.py`** — recursive and tail-recursive implementations of `factorial`, string `length`, `power`, and `remove_vowels`.
- **`fibtreerecursion.py`** — memoized recursive Fibonacci (`fib_memo`), prints `fib(0)` through `fib(40)`.
- **`even_fibonacci.py`** — sums even-valued Fibonacci terms below a given limit.
- **`sqrt.py`** — computes square roots via Newton's method (`sqrt(num, epsilon)`). CLI usage: `python sqrt.py <value> [epsilon]`.
- **`unit_tests_py.py`** — `unittest` suite covering `sqrt.py`'s CLI behavior (usage errors, `inf`/`nan` handling, precision). Run with `python unit_tests_py.py` or `pytest`.
- **`listmethods.py`** — a scratch script demonstrating common Python `list` methods (`append`, `extend`, `insert`, `remove`, `pop`, `sort`, `copy`, etc.).
- **`processargs.py`** — CLI demo that parses two integer args and prints their max. Usage: `python processargs.py <num1> <num2>`.

### `searching/`

- **`searchcomparison.py`** — compares linear search vs. binary search runtime over a randomly generated, sorted list of integers. Prompts for list size and number of keys, then prints execution time for each. Run with `python searchcomparison.py`.

### `graphs/`

- **`leetcodeRottenOranges.py`** — solution to LeetCode's [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/), using multi-source BFS. `Solution.orangesRotting(grid)` returns minutes until no fresh orange remains, or `-1` if impossible.
- **`toposort.py`** — topological sort of a directed graph using Kahn's algorithm with a min-heap (always expands the lowest-numbered available node). Reads `n m` followed by `m` edges from stdin; prints the topological order, or a failure message if the graph has a cycle.
- **`path_sum_two_ways.py`** — solution to Project Euler #81 (minimal path sum through a grid moving only right or down), via dynamic programming. Reads a CSV grid from `matrix.txt` in the same directory; prints the minimum sum and the values along the optimal path.
- **`matrix.txt`** — input grid data used by `path_sum_two_ways.py`.

### `project_euler/`

- **`problem0euler.py`** — sums the squares of every second integer up to 655,000 (uses `pandas`).
- **`problem1euler.py`** — Project Euler #1: sum of all multiples of 3 or 5 below 1000.
- **`problem2euler.py`** — Project Euler #2-style Fibonacci generator/exploration (even-term sum logic is present but not printed).
- **`problem3euler.py`** — Project Euler #3: largest prime factor of 600,851,475,143.

## Requirements

Python 3. Most scripts use only the standard library; `problem0euler.py` and the (commented-out) alternate versions in `project_euler/` require `pandas`.
