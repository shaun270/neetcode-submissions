from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r: int, c: int, current_dist: int) -> None:
            # Boundary check
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            # Obstacle check
            if grid[r][c] == -1:
                return
            # Pruning: If we reached a cell but our current path distance is 
            # GREATER than or EQUAL to a path already found, stop exploring.
            if current_dist > grid[r][c]:
                return
                
            # Update the cell with the shorter distance found
            grid[r][c] = current_dist
            
            # Explore all 4 neighbors with an incremented distance
            dfs(r + 1, c, current_dist + 1)
            dfs(r - 1, c, current_dist + 1)
            dfs(r, c + 1, current_dist + 1)
            dfs(r, c - 1, current_dist + 1)

        # Step 1: Find all treasures (0) and kick off DFS from them
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    # Start DFS from the treasure with a starting distance of 0
                    dfs(i, j, 0)