# shape_columbia

A small collection of data structures and algorithms exercises in Python.

## Contents

### `MyLinkedList.py`
A doubly linked list implemented from scratch with deque-style operations.

- `append(element)` / `appendleft(element)` — insert at the right/left end
- `pop()` / `popleft()` — remove and return from the right/left end
- `get(index)` / `set(index, element)` — indexed access via `[]`
- `rotate(n)` — rotate elements `n` steps to the right (negative rotates left)
- `is_empty()`, `__len__`, `__iter__`, `__repr__`

Run it directly to see a demo:

```bash
python3 MyLinkedList.py
```

### `searchcomparison.py`
Compares the runtime of linear search vs. binary search over a randomly generated, sorted list of integers.

- `linear_search(lst, key)` — O(n) scan for `key`
- `binary_search(lst, key)` — O(log n) search over a sorted list
- `create_list_of_random_ints(length, a, b, sort=False)` — helper to generate test data

Run it and follow the prompts to enter a list size and number of keys to search for; it prints the execution time for each approach:

```bash
python3 searchcomparison.py
```

### `leetcodeRottenOranges.py`
Solution to LeetCode's [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) problem, solved with a multi-source BFS.

- `Solution.orangesRotting(grid)` — returns the number of minutes until no fresh orange remains, or `-1` if that's impossible

## Requirements

Python 3, standard library only (no external dependencies).