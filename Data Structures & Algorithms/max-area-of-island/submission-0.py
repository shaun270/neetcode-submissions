from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        max_area = 0
        
        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            
            current_area = 1
            
            for d in directions:
                current_area += dfs(row + d[0], col + d[1])
                
            return current_area
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    max_area = max(area, max_area)
        
        return max_area