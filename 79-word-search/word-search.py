class Solution(object):
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, index):
            # Entire word found
            if index == len(word):
                return True

            # Invalid position or character does not match
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or board[row][col] != word[index]
            ):
                return False

            # Mark current cell as visited
            temp = board[row][col]
            board[row][col] = "#"

            # Search in all four directions
            found = (
                dfs(row + 1, col, index + 1)
                or dfs(row - 1, col, index + 1)
                or dfs(row, col + 1, index + 1)
                or dfs(row, col - 1, index + 1)
            )

            # Backtrack: restore the cell
            board[row][col] = temp

            return found

        # Try every cell as the starting point
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False