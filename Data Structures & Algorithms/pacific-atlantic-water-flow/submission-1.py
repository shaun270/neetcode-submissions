class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific_set = set()
        atlantic_set = set()
        result = []

        def dfs(i, j, which_set, prev):
            if (i < 0 or j < 0 or i >= ROWS or j >= COLS or heights[i][j] < prev or (i, j) in which_set):
                return 

            which_set.add((i, j))
            dfs(i + 1, j, which_set, heights[i][j])
            dfs(i - 1, j, which_set, heights[i][j])
            dfs(i, j + 1, which_set, heights[i][j])
            dfs(i, j - 1, which_set, heights[i][j])

        for j in range(COLS):
            dfs(0, j, pacific_set, heights[0][j])
            dfs(ROWS-1, j, atlantic_set, heights[ROWS-1][j])

        for i in range(ROWS):
            dfs(i, 0, pacific_set, heights[i][0])
            dfs(i, COLS - 1, atlantic_set, heights[i][COLS - 1])

        print(pacific_set)
        print(atlantic_set)
        common_tuples = pacific_set & atlantic_set

        return list(common_tuples)

            
