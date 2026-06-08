from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        step = 0
        q = deque()
        has_fresh = any(1 in row for row in grid)
        if not has_fresh:
            return 0
        def add_cell(r, c):
            nonlocal has_next
            if (r >= ROWS or c >= COLS or r < 0 or c < 0 or (r,c) in visited or grid[r][c] == 0):
                return
            
            q.append((r, c))
            visited[r][c] = True
            has_next = True

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited[i][j] = True

        while q:
            has_next = False
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 0
                add_cell(r + 1, c)
                add_cell(r - 1, c)
                add_cell(r, c + 1)
                add_cell(r, c - 1)
            if has_next and any(1 in row for row in grid):
                step+=1

        if any(1 in row for row in grid):
            return -1        
        return step



