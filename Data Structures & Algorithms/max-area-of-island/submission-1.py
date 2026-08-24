class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        row, col = len(grid), len(grid[0])
        island_area = 0

        def dfs(i, j):
            if i >= row or i < 0 or j >= col or j < 0 or grid[i][j] == 0:
                return 0
            curr_area = 1
            grid[i][j] = 0
            for dx, dy in directions:
                curr_area += dfs(i + dx, j + dy)

            return curr_area
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    island_area = max(island_area, dfs(i, j))
        
        return island_area