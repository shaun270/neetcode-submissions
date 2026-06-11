class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        X_set = set()
        O_set = set()
        temp_set = set()
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'X':
                    X_set.add((i, j))
                else:
                    O_set.add((i, j))
        full_set = X_set | O_set

        def dfs(i, j, temp):
            if (i<0 or j<0 or i==ROWS or j==COLS or (i, j) in temp or (i, j) in X_set):
                return 
            
            temp.add((i, j))
            dfs(i + 1, j, temp)
            dfs(i - 1, j, temp)
            dfs(i, j + 1, temp)
            dfs(i, j - 1, temp)

        for j in range(COLS):
                dfs(0, j, temp_set)
                dfs(ROWS - 1, j, temp_set)
        
        for i in range(ROWS):
                dfs(i, COLS - 1, temp_set)
                dfs(i, 0, temp_set)

        result = full_set - temp_set
        print(temp_set)
        for dx, dy in result:
            board[dx][dy] = 'X'

        # keep a temp set, start from borders, do dfs traversal and mark all those in temp set
        # full_set - temp_set = our final X's