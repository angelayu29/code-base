class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute = 0
        rotten = deque()
        fresh = 0
        row, col = len(grid), len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while rotten and fresh > 0:
            for i in range(len(rotten)):
                r, c = rotten.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        rotten.append([nr, nc])
            minute += 1

        return minute if fresh == 0 else -1

